#!/usr/bin/env python3
"""Build the Backup Basics Handbook static site.

Converts the Markdown in docs/ into a static HTML site in site/ using only
the Python standard library, so the project stays local-first and
dependency-free. Run via build.sh or: python3 build.py
"""

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
SITE = ROOT / "site"
ASSETS = ROOT / "assets"

# Ordered site map: (markdown path relative to docs/, site path, pager label)
PAGES = [
    ("index.md", "index.html", "Home"),
    ("01-what-needs-backing-up.md", "01-what-needs-backing-up.html", "What to back up"),
    ("02-the-3-2-1-rule.md", "02-the-3-2-1-rule.html", "3-2-1 rule"),
    ("03-external-drive-routines.md", "03-external-drive-routines.html", "Drive routines"),
    ("04-free-cloud-vs-local.md", "04-free-cloud-vs-local.html", "Cloud vs local"),
    ("05-phone-photo-backups.md", "05-phone-photo-backups.html", "Phone photos"),
    ("06-formats-that-last.md", "06-formats-that-last.html", "Formats that last"),
    ("07-restore-drills.md", "07-restore-drills.html", "Restore drills"),
    ("08-after-a-crash.md", "08-after-a-crash.html", "After a crash"),
    ("worksheet.md", "worksheet.html", "Worksheet"),
    ("glossary.md", "glossary.html", "Glossary"),
    ("recipes/index.md", "recipes/index.html", "Recipes"),
    ("recipes/recipe-01-first-copy.md", "recipes/recipe-01-first-copy.html", "Recipe 1 - First copy"),
    ("recipes/recipe-02-restore-drill.md", "recipes/recipe-02-restore-drill.html", "Recipe 2 - Restore drill"),
    ("recipes/recipe-03-auto-backup.md", "recipes/recipe-03-auto-backup.html", "Recipe 3 - Auto backups"),
    ("recipes/recipe-04-cloud-folder.md", "recipes/recipe-04-cloud-folder.html", "Recipe 4 - Cloud folder"),
    ("recipes/recipe-05-yearly-archive-check.md", "recipes/recipe-05-yearly-archive-check.html", "Recipe 5 - Yearly check"),
]

SITE_TITLE = "The Backup Basics Handbook"

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — {site_title}</title>
<link rel="stylesheet" href="{style_href}styles.css">
</head>
<body{page_class}>
{nav}
<main class="page">
<h1 class="page-title">{heading}</h1>
{hero}
{body}
{prev_next}
</main>
<footer class="site-footer">
<p>The Backup Basics Handbook &middot; built by <strong>Asdale Dynamics, LLC</strong> &middot; MIT licensed &middot; works offline</p>
</footer>
</body>
</html>
"""


def escape(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def inline(text):
    """Render inline markdown on already-escaped text."""
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)",
                  lambda m: '<a href="%s">%s</a>' % (m.group(2), m.group(1)),
                  text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", text)
    return text


def table_cells(line):
    s = line.strip().strip("|")
    return [c.strip() for c in s.split("|")]


def is_table_row(line):
    s = line.strip()
    return s.startswith("|") and s.endswith("|") and s.count("|") >= 2


def is_table_sep(line):
    s = line.strip()
    if not s.startswith("|"):
        return False
    return bool(re.fullmatch(r"\|(?:\s*:-{2,}\s*\|)+", s))


def render_markdown(md_text):
    """Convert a small, friendly subset of Markdown to HTML blocks."""
    lines = md_text.splitlines()
    out = []
    i = 0
    n = len(lines)
    para_buf = []

    def flush_para():
        if para_buf:
            out.append("<p>%s</p>" % inline(escape(" ".join(para_buf)).strip()))
            para_buf.clear()

    while i < n:
        stripped = lines[i].strip()

        if stripped.startswith("```"):
            flush_para()
            lang = stripped[3:].strip()
            code_lines = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            i += 1  # skip closing fence
            cls = ' class="lang-%s"' % lang if lang else ""
            out.append("<pre%s><code>%s</code></pre>"
                       % (cls, escape("\n".join(code_lines))))
            continue

        if not stripped:
            flush_para()
            i += 1
            continue

        m = re.match(r"^(#{1,4})\s+(.*)$", stripped)
        if m:
            flush_para()
            level = len(m.group(1))
            out.append("<h%d>%s</h%d>" % (level, inline(escape(m.group(2))), level))
            i += 1
            continue

        if re.fullmatch(r"-{3,}", stripped):
            flush_para()
            out.append("<hr>")
            i += 1
            continue

        if stripped.startswith(">"):
            flush_para()
            quote = []
            while i < n and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip()[1:].strip())
                i += 1
            out.append("<blockquote><p>%s</p></blockquote>"
                       % inline(escape(" ".join(quote))))
            continue

        if is_table_row(stripped) and i + 1 < n and is_table_sep(lines[i + 1]):
            flush_para()
            head = table_cells(stripped)
            i += 2
            rows = []
            while i < n and is_table_row(lines[i]):
                rows.append(table_cells(lines[i].strip()))
                i += 1
            head_html = "".join("<th>%s</th>" % inline(escape(c)) for c in head)
            body_html = "".join(
                "<tr>%s</tr>" % "".join("<td>%s</td>" % inline(escape(c)) for c in row)
                for row in rows)
            out.append("<table><thead><tr>%s</tr></thead><tbody>%s</tbody></table>"
                       % (head_html, body_html))
            continue

        if re.match(r"^\d+\.\s", stripped):
            flush_para()
            items = []
            while i < n:
                item_m = re.match(r"^(\d+)\.\s+(.*)$", lines[i].strip())
                if not item_m:
                    break
                items.append(item_m.group(2))
                i += 1
            out.append("<ol>%s</ol>"
                       % "".join("<li>%s</li>" % inline(escape(t)) for t in items))
            continue

        if re.match(r"^-\s+", stripped):
            flush_para()
            items = []
            while i < n:
                item_m = re.match(r"^-\s+(.*)$", lines[i].strip())
                if not item_m:
                    break
                item = item_m.group(1)
                cb = re.match(r"^\[([ xX])\]\s*(.*)$", item)
                if cb:
                    mark = " checked" if cb.group(1).lower() == "x" else ""
                    items.append('<li class="check"><span class="box%s"></span>%s</li>'
                                 % (mark, inline(escape(cb.group(2)))))
                else:
                    items.append("<li>%s</li>" % inline(escape(item)))
                i += 1
            out.append("<ul>%s</ul>" % "".join(items))
            continue

        para_buf.append(stripped)
        i += 1

    flush_para()
    return "\n".join(out)


def split_heading(md_path):
    """Return (title, body_text) with the leading '# ' heading removed."""
    lines = md_path.read_text(encoding="utf-8").splitlines()
    title = SITE_TITLE
    if lines and lines[0].startswith("# "):
        title = lines[0][2:].strip()
        lines = lines[1:]
    while lines and not lines[0].strip():
        lines = lines[1:]
    return title, "\n".join(lines)


def page_title(md_path):
    return split_heading(md_path)[0]


def build_nav(current_html_rel, depth):
    parts = []
    for _, site_path, label in PAGES:
        href = ("../" * depth) + site_path
        cls = ' class="here"' if site_path == current_html_rel else ""
        parts.append('<li><a href="%s"%s>%s</a></li>' % (href, cls, label))
    return '<nav class="site-nav"><ul>%s</ul></nav>' % "".join(parts)


def build_prev_next(html_rel, depth):
    idx = [p[1] for p in PAGES].index(html_rel)
    links = []
    if idx > 0:
        prev_path, prev_label = PAGES[idx - 1][1], PAGES[idx - 1][2]
        links.append('<a class="pager-link" href="%s%s">&larr; %s</a>'
                     % ("../" * depth, prev_path, prev_label))
    if idx + 1 < len(PAGES):
        next_path, next_label = PAGES[idx + 1][1], PAGES[idx + 1][2]
        links.append('<a class="pager-link pager-next" href="%s%s">%s &rarr;</a>'
                     % ("../" * depth, next_path, next_label))
    return '<div class="pager">%s</div>' % "".join(links) if links else ""


def build_page(md_rel, html_rel, depth):
    md_path = DOCS / md_rel
    title, md_text = split_heading(md_path)
    body = render_markdown(md_text)
    heading = "The Backup Basics Handbook" if md_rel == "index.md" else title
    hero = ('<p class="hero-note"><em>Never lose your stuff again — '
            'explained like a friend would.</em></p>'
            if md_rel == "index.md" else "")
    nav = build_nav(html_rel, depth)
    prev_next = build_prev_next(html_rel, depth)
    page_class = ' class="worksheet-page"' if "worksheet" in html_rel else ""
    html_doc = TEMPLATE.format(
        title=title,
        site_title=SITE_TITLE,
        style_href="../" * depth,
        heading=heading,
        hero=hero,
        page_class=page_class,
        nav=nav,
        body=body,
        prev_next=prev_next,
    )
    out_path = SITE / html_rel
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html_doc, encoding="utf-8")


def main():
    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir(parents=True)

    for md_rel, html_rel, _label in PAGES:
        depth = 1 if "/" in html_rel else 0
        build_page(md_rel, html_rel, depth)

    shutil.copy2(ASSETS / "styles.css", SITE / "styles.css")

    print("Built %d pages into site/" % len(PAGES))


if __name__ == "__main__":
    main()
