import argparse
import base64
import logging
import os
import re
import shutil
import subprocess
import tempfile

import markdown

preamble = """\
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<style>
{css}
</style>
</head>
<body>
<div id="resume">
"""

postamble = """\
</div>
</body>
</html>
"""

CHROME_GUESSES_MACOS = (
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
)


def guess_chrome_path() -> str:
    for guess in CHROME_GUESSES_MACOS:
        if os.path.exists(guess):
            logging.info("Found Chrome or Chromium at " + guess)
            return guess
    raise ValueError("Could not find Chrome. Please set CHROME_PATH.")


def title(md: str) -> str:
    """
    Return the contents of the first markdown heading in md, which we
    assume to be the title of the document.
    """
    for line in md.splitlines():
        if re.match("^#[^#]", line):  # starts with exactly one '#'
            return line.lstrip("#").strip()
    raise ValueError(
        "Cannot find any lines that look like markdown h1 headings to use as the title"
    )


def make_html(md: str, prefix: str = "resume") -> str:
    """
    Compile md to HTML and prepend/append preamble/postamble.

    Insert <prefix>.css if it exists.
    """
    try:
        with open(prefix + ".css") as cssfp:
            css = cssfp.read()
    except FileNotFoundError:
        print(prefix + ".css not found. Output will by unstyled.")
        css = ""
    return "".join(
        (
            preamble.format(title=title(md), css=css),
            markdown.markdown(md, extensions=["smarty", "abbr"]),
            postamble,
        )
    )


def write_pdf(html: str, prefix: str = "resume") -> None:
    """
    Write html to prefix.pdf
    """
    chrome = guess_chrome_path()
    html64 = base64.b64encode(html.encode("utf-8"))
    options = [
        "--no-sandbox",
        "--headless",
        "--print-to-pdf-no-header",
        # Keep both versions of this option for backwards compatibility
        # https://developer.chrome.com/docs/chromium/new-headless.
        "--no-pdf-header-footer",
        "--enable-logging=stderr",
        "--log-level=2",
        "--in-process-gpu",
        "--disable-gpu",
    ]

    subprocess.run(
        [
            chrome,
            *options,
            f"--print-to-pdf={prefix}.pdf",
            "data:text/html;base64," + html64.decode("utf-8"),
        ],
        timeout=1.0,
        stderr=subprocess.DEVNULL,
    )
    logging.info(f"Wrote {prefix}.pdf")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "file",
        help="html input file [resume.html]",
        default="resume.html",
        nargs="?",
    )
    parser.add_argument("-q", "--quiet", action="store_true")
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()

    if args.quiet:
        logging.basicConfig(level=logging.WARN, format="%(message)s")
    elif args.debug:
        logging.basicConfig(level=logging.DEBUG, format="%(message)s")
    else:
        logging.basicConfig(level=logging.INFO, format="%(message)s")

    prefix, _ = os.path.splitext(os.path.abspath(args.file))

    with open(args.file, encoding="utf-8") as htmlfp:
        html = htmlfp.read()
    write_pdf(html, prefix=prefix)
