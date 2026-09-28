# Seonghwan Seo — personal website

Source for [SeonghwanSeo.github.io](https://SeonghwanSeo.github.io), built with Jekyll and the [al-folio](https://github.com/alshedivat/al-folio) theme.

## Content

| Content                              | Source                                             |
| ------------------------------------ | -------------------------------------------------- |
| Introduction and research highlights | `_pages/about.md`                                  |
| Publications                         | `_bibliography/papers.bib`                         |
| Research projects                    | `_projects/`                                       |
| News                                 | `_news/`                                           |
| Web CV                               | `_data/cv.yml` and `_pages/cv.md`                  |
| Downloadable CV                      | `assets/pdf/resume.html` → `assets/pdf/resume.pdf` |
| Social links                         | `_data/socials.yml`                                |
| Site settings                        | `_config.yml`                                      |

## Local preview

With Docker running, from the repository root:

```sh
docker compose up
```

Open [localhost:8080](http://localhost:8080). Stop the preview with `Ctrl+C`.

## Update the CV PDF

Edit `assets/pdf/resume.html`, then run:

```sh
python3 scripts/build-resume-pdf.py
```

Chrome or Chromium is required. The script uses A4 print styles and disables browser headers and footers. Inspect every PDF page for clipping and confirm the final section is present. Keep the generated PDF at `assets/pdf/resume.pdf`, which the CV page links to.

## Deployment and checks

`.github/workflows/deploy.yml` builds the site and deploys `_site/` to `gh-pages` on matching pushes to `main` or `master`. Pull requests run the build without deployment; manual dispatch is also available.

The repository retains workflows for broken links, accessibility, CodeQL, and formatting. Docker configuration, theme layouts, includes, styles, and plugins support local development and site generation.

## Theme

The site uses [al-folio](https://github.com/alshedivat/al-folio). Refer to the upstream documentation for theme customization. The original MIT license is retained in [LICENSE](LICENSE).
