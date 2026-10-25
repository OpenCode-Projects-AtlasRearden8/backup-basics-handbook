# STATUS — Backup Basics Handbook

Created: 2026-10-25

## What was built

A beginner-friendly handbook ("never lose your stuff again, friend-style")
delivered as Markdown sources plus a dependency-free static site build.

- **docs/** — 11 main documents: welcome/index, "what actually needs
  backing up", the 3-2-1 rule in plain words, external-drive routines,
  free cloud vs local trade-offs, phone photo backups, ten-year-proof file
  formats, restore drills, after-a-crash recovery steps, a printable
  backup-plan worksheet, and a plain-English glossary.
- **docs/recipes/** — 5 short recipes (first copy, restore drill, OS
  automatic backups, cloud folder, yearly archive check), each with "check
  your work" and an honest note on where it was tested.
- **build.py / build.sh** — static site generator using only the Python
  standard library (no pip packages, no network). Reads docs/, writes
  site/ (17 HTML pages + one stylesheet), full nav, prev/next pagers,
  print-ready styling for the worksheet page.
- **assets/styles.css** — the one stylesheet, warm paper theme, print
  media rules (nav/footer hidden, checkboxes printable).
- **README.md** — overview, build/run instructions, credited to
  Asdale Dynamics, LLC.
- **LICENSE** — MIT, copyright line exactly `Copyright (c) 2026 Asdale Dynamics, LLC`.
- **test.py / test.sh** — automated verification (details below).

Content style: warm, plain-English, step-by-step, ADHD-friendly short
actions ("Do this today" boxes), local-first throughout (no accounts or
network required to read, build, or test).

## How to run it

```sh
./build.sh    # builds the static site into site/
./test.sh     # rebuilds and runs all verification checks
```

Read `site/index.html` in any browser. Everything works fully offline.

## Verification results (all passing)

`./test.sh` output — 10/10 PASS:

- build.sh exits cleanly (17 pages built)
- all expected site files exist (17 HTML + styles.css)
- every internal link resolves (nav, TOC links, recipes cross-links)
- LICENSE contains the exact required copyright line
- README credits Asdale Dynamics, LLC
- every HTML page has a title, the stylesheet link, and the footer credit
- worksheet renders printable checkboxes (6 rhythm checklists)
- print stylesheet hides site nav/footer
- no unrendered markdown (stray `[..](..)` ) in any HTML
- **Recipe shell commands verified**: the recipe-2 sequence (mkdir, copy,
  delete original, restore, checksum compare) and the recipe-5 commands
  (du, find, count, empty-file scan) were executed in a sandboxed temp
  directory; restore produced a byte-identical file (matching `cksum`).

## Known gaps

- GUI recipes (Windows File History, macOS Time Machine, provider cloud
  apps) were written from official documentation; they could not be
  exercised on this Linux-only build machine, so menu labels may have
  drifted. Each carries an honest tested-note in-page.
- Free-tier sizes quoted (iCloud 5 GB, Google 15 GB, OneDrive 5 GB,
  Dropbox ~2 GB) are "as of writing"; the book tells readers to check
  current terms.
- The markdown converter implements the friendly subset the handbook uses
  (headings, lists, checkboxes, tables, blockquotes, fenced code, bold/
  italic, links). It is not a general Markdown parser; unsupported syntax
  would render as plain text rather than fail the build.
- Screenshots/illustrations: none; intentionally text-and-tables so it
  prints cleanly and stays dependency-free.
- Site is committed but not deployed anywhere (per instructions: no
  publishing, no remote).

## Git

Committed locally on a fresh repository with the existing git identity.
No push, no remote, no co-author trailers.
