# Task naming

- Prefix Codex task names with `[C]`.
- Prefix review-focused Codex task names with `[R]`.
- Prefix ChatGPT Work task names with `[W]`.

# CV PDF

- Edit `assets/pdf/resume.html` as the source for the downloadable CV. `_pages/cv.md` points to `assets/pdf/resume.pdf`.
- After changing the HTML, run `python3 scripts/build-resume-pdf.py` from the repository root to regenerate `assets/pdf/resume.pdf` with Chrome's print engine.
- The script uses the HTML's A4 print CSS and disables Chrome's date/title header and file-path/page-number footer. Do not use Chrome's default `--print-to-pdf` output without `--no-pdf-header-footer`.
- Check the PDF page count and render every page for visual inspection. Confirm the final section is present, no content is clipped, and no browser-generated header or footer appears.
- Keep the generated PDF in `assets/pdf/resume.pdf`; do not move it to a generic output directory because the site links to this path.
