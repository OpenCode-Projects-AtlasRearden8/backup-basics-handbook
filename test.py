#!/usr/bin/env python3
"""Verification for The Backup Basics Handbook.

Checks that the build is complete and sane, that internal links resolve,
that the required credits are present, and that the shell commands in
Recipe 2 (restore drill) really work when run end to end.
"""

import re
import shutil
import subprocess
import sys
import tempfile
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = ROOT / "site"

FAILURES = []


def check(name, ok, detail=""):
    print("%s %s%s" % ("PASS" if ok else "FAIL", name, (" - " + detail) if detail else ""))
    if not ok:
        FAILURES.append(name)


class LinkGrabber(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        for key in ("href", "src"):
            if key in d:
                self.links.append(d[key])


def build():
    result = subprocess.run(["./build.sh"], cwd=ROOT, capture_output=True, text=True)
    check("build.sh exits cleanly", result.returncode == 0, result.stdout.strip())
    return result.returncode == 0


EXPECTED_PAGES = [
    "index.html",
    "01-what-needs-backing-up.html",
    "02-the-3-2-1-rule.html",
    "03-external-drive-routines.html",
    "04-free-cloud-vs-local.html",
    "05-phone-photo-backups.html",
    "06-formats-that-last.html",
    "07-restore-drills.html",
    "08-after-a-crash.html",
    "worksheet.html",
    "glossary.html",
    "recipes/index.html",
    "recipes/recipe-01-first-copy.html",
    "recipes/recipe-02-restore-drill.html",
    "recipes/recipe-03-auto-backup.html",
    "recipes/recipe-04-cloud-folder.html",
    "recipes/recipe-05-yearly-archive-check.html",
    "styles.css",
]


def check_pages():
    missing = [p for p in EXPECTED_PAGES if not (SITE / p).is_file()]
    check("all expected site files exist", not missing, ", ".join(missing) or "17 pages + css")


def check_links():
    all_links_ok = True
    bad = []
    for page in [p for p in EXPECTED_PAGES if p.endswith(".html")]:
        html_text = (SITE / page).read_text(encoding="utf-8")
        grabber = LinkGrabber()
        grabber.feed(html_text)
        base = (SITE / page).parent
        for href in grabber.links:
            if href.startswith("#") or href.startswith("http"):
                continue
            target = (base / href).resolve()
            if not target.is_file():
                all_links_ok = False
                bad.append("%s -> %s" % (page, href))
    check("every internal link resolves", all_links_ok, "; ".join(bad) or "all resolve")


def check_structure_and_credits():
    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    check("LICENSE has exact copyright line",
          "Copyright (c) 2026 Asdale Dynamics, LLC" in license_text)

    readme_text = (ROOT / "README.md").read_text(encoding="utf-8")
    check("README credits Asdale Dynamics, LLC",
          "Asdale Dynamics, LLC" in readme_text)

    missing_footer = []
    for page in [p for p in EXPECTED_PAGES if p.endswith(".html")]:
        text = (SITE / page).read_text(encoding="utf-8")
        if "Asdale Dynamics, LLC" not in text:
            missing_footer.append(page)
        if "<title>" not in text or "styles.css" not in text:
            missing_footer.append(page)
    check("every HTML page has title, stylesheet, and credit line",
          not missing_footer, ", ".join(sorted(set(missing_footer))) or "all pages")

    # worksheet must have printable checkbox content and no nav in print css
    ws = (SITE / "worksheet.html").read_text(encoding="utf-8")
    check("worksheet renders checklists", ws.count('class="check"') >= 6)
    css = (SITE / "styles.css").read_text(encoding="utf-8")
    check("print stylesheet hides the site nav", "@media print" in css and ".site-nav" in css)

    # no stray unrendered markdown in the HTML
    strays = []
    for page in [p for p in EXPECTED_PAGES if p.endswith(".html")]:
        text = (SITE / page).read_text(encoding="utf-8")
        if re.search(r"(\[.*\]\(.*\))", text):
            strays.append(page)
    check("no unrendered markdown links remain", not strays, ", ".join(strays) or "clean")


def check_recipe_commands():
    """Run the Recipe 2 command sequence, sandboxed, and verify the restore."""
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        home = tmp / "home"
        drive = tmp / "drive"
        home.mkdir()
        drive.mkdir()
        script = f"""
set -e
export HOME={home}
mkdir -p ~/drill-demo/treasures
echo "the trilogy draft" > ~/drill-demo/treasures/trilogy-draft.txt
mkdir -p {drive}/Backups/treasures
cp -aut {drive}/Backups/treasures/ ~/drill-demo/treasures/.
cp ~/drill-demo/treasures/trilogy-draft.txt {tmp}/trilogy-safe.txt
rm ~/drill-demo/treasures/trilogy-draft.txt
if ls ~/drill-demo/treasures/trilogy-draft.txt >/dev/null 2>&1; then
  echo "UNEXPECTED: file still present after deletion"; exit 1
fi
cp -aut ~/drill-demo/treasures/ {drive}/Backups/treasures/.
cksum {tmp}/trilogy-safe.txt ~/drill-demo/treasures/trilogy-draft.txt
"""
        result = subprocess.run(["bash", "-c", script], capture_output=True, text=True)
        ok = result.returncode == 0
        detail = "restore drill commands work end to end"
        if ok:
            lines = [l for l in result.stdout.strip().splitlines() if l.strip()]
            sums = {l.split()[0] for l in lines}
            if len(lines) != 2 or len(sums) != 1:
                ok = False
                detail = "checksums did not match: %r" % result.stdout
        else:
            detail = "command failed: %s" % (result.stderr.strip() or result.stdout.strip())

        # also verify the archive-check recipe commands behave
        script2 = f"""
set -e
du -ah {drive}/Backups/ | sort -rh | head -20 >/dev/null
find {drive}/Backups/ -type f \\( -iname "*.txt" -o -iname "*.pdf" \\) | wc -l >/dev/null
find {drive}/Backups/ -type f -empty | wc -l
"""
        result2 = subprocess.run(["bash", "-c", script2], capture_output=True, text=True)
        if result2.returncode != 0:
            ok = False
            detail = "archive-check commands failed: %s" % result2.stderr.strip()

        check("recipe shell commands verified (copy, delete, restore, checksum)", ok, detail)


def main():
    ok = build()
    if ok:
        check_pages()
        check_links()
        check_structure_and_credits()
        check_recipe_commands()

    if FAILURES:
        print("\n%d check(s) FAILED: %s" % (len(FAILURES), ", ".join(FAILURES)))
        return 1
    print("\nAll checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
