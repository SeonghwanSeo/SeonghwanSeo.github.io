#!/usr/bin/env python3
"""Print the CV HTML to its published PDF path using Chrome."""

import os
import shutil
import signal
import subprocess
import sys
import tempfile
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets/pdf/resume.html"
OUTPUT = ROOT / "assets/pdf/resume.pdf"


def chrome_path():
    candidates = [
        Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"),
        Path("/usr/bin/google-chrome"),
        Path("/usr/bin/chromium"),
    ]
    for name in ("google-chrome", "chromium", "chromium-browser"):
        found = shutil.which(name)
        if found:
            candidates.append(Path(found))
    return next((path for path in candidates if path.is_file()), None)


def main():
    chrome = chrome_path()
    if chrome is None:
        raise SystemExit("Chrome or Chromium is required to build resume.pdf")
    if not SOURCE.is_file():
        raise SystemExit(f"Missing source: {SOURCE}")

    with tempfile.TemporaryDirectory(prefix="resume-pdf-") as temp_dir:
        temp = Path(temp_dir)
        draft = temp / "resume.pdf"
        command = [
            str(chrome),
            "--headless",
            "--disable-gpu",
            "--no-first-run",
            "--no-default-browser-check",
            "--no-pdf-header-footer",
            f"--user-data-dir={temp / 'chrome-profile'}",
            f"--print-to-pdf={draft}",
            SOURCE.as_uri(),
        ]
        process = subprocess.Popen(
            command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            start_new_session=True,
        )
        try:
            deadline = time.monotonic() + 30
            last_size = -1
            stable_since = None
            while time.monotonic() < deadline:
                if draft.exists():
                    size = draft.stat().st_size
                    if size == last_size and size > 1000:
                        stable_since = stable_since or time.monotonic()
                        if time.monotonic() - stable_since >= 0.5:
                            break
                    else:
                        last_size = size
                        stable_since = None
                if process.poll() is not None and not draft.exists():
                    raise RuntimeError(f"Chrome exited before writing PDF (code {process.returncode})")
                time.sleep(0.1)
            else:
                raise TimeoutError("Chrome did not finish the PDF within 30 seconds")

            with draft.open("rb") as pdf:
                if pdf.read(5) != b"%PDF-":
                    raise RuntimeError("Chrome produced an invalid PDF")
                pdf.seek(-1024, os.SEEK_END)
                if b"%%EOF" not in pdf.read():
                    raise RuntimeError("Chrome produced an incomplete PDF")
            os.replace(draft, OUTPUT)
            print(f"Wrote {OUTPUT}")
        finally:
            if process.poll() is None:
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=3)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait()


if __name__ == "__main__":
    try:
        main()
    except (OSError, RuntimeError, TimeoutError) as error:
        print(error, file=sys.stderr)
        raise SystemExit(1)
