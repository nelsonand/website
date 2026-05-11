import bibtexparser
from collections import defaultdict
import re

INPUT_FILE = "cv_prep.bib"
OUTPUT_FILE = "publications.md"

FRONT_MATTER = """---
layout: page
title: Publications
full-width: true
---

"""


# ----------------------------
# Helpers
# ----------------------------

def clean(text):
    if not text:
        return ""
    return re.sub(r"[{}]", "", text).strip()


def get_year(entry):
    # Zotero exports use 'date'; traditional BibTeX uses 'year'
    raw = entry.get("year") or entry.get("date") or "0"
    return int(str(raw)[:4]) if raw else 0


def has_keyword(entry, key):
    keywords = entry.get("keywords", "")
    keyword_list = [k.strip() for k in keywords.split(",")]
    return key in keyword_list


AUTHOR_THRESHOLD = 20


def format_single_author(raw):
    """Convert 'Last, First' → 'First Last', strip braces, bold Nelson."""
    raw = raw.strip()
    if "," in raw:
        last, first = [x.strip() for x in raw.split(",", 1)]
        name = f"{first} {last}"
    else:
        name = raw
    name = re.sub(r"[{}]", "", name)
    if re.search(r"\bA\.?\s*O\.?\s+Nelson\b", name, re.IGNORECASE):
        name = f"**{name}**"
    return name


def format_authors(author_field):
    authors = [a.strip() for a in author_field.split(" and ")]

    if len(authors) <= AUTHOR_THRESHOLD:
        return ", ".join(format_single_author(a) for a in authors)

    # Long list: find Nelson's position (0-indexed)
    nelson_idx = None
    for i, a in enumerate(authors):
        raw = a.strip()
        if "," in raw:
            last, first = [x.strip() for x in raw.split(",", 1)]
            name = f"{first} {last}"
        else:
            name = raw
        name = re.sub(r"[{}]", "", name)
        if re.search(r"\bA\.?\s*O\.?\s+Nelson\b", name, re.IGNORECASE):
            nelson_idx = i
            break

    if nelson_idx is not None and nelson_idx < AUTHOR_THRESHOLD:
        # Nelson appears within the threshold: show up to and including his name
        keep = [format_single_author(a) for a in authors[: nelson_idx + 1]]
        suffix = ", et al." if nelson_idx + 1 < len(authors) else ""
        return ", ".join(keep) + suffix
    else:
        # Nelson is deep in the list or absent: just show the first author
        return format_single_author(authors[0]) + " et al."


def format_entry(entry):
    authors = format_authors(entry.get("author", ""))
    title = clean(entry.get("title", ""))
    # Zotero exports use 'journaltitle'; traditional BibTeX uses 'journal'
    venue = clean(
        entry.get("journal") or entry.get("journaltitle") or entry.get("booktitle") or ""
    )
    year = get_year(entry)
    volume = entry.get("volume", "")
    number = entry.get("number", "")
    pages = entry.get("pages", "")
    doi = entry.get("doi", "")
    url = entry.get("url", "")

    citation = f"{authors} ({year}). *{title}*."

    if venue:
        citation += f" **{venue}**"

    if volume:
        citation += f", {volume}"
        if number:
            citation += f"({number})"

    if pages:
        citation += f", {pages}"

    citation += "."

    if doi:
        citation += f" [DOI](https://doi.org/{doi})"
    elif url:
        citation += f" [Link]({url})"

    return citation


# ----------------------------
# Main Logic
# ----------------------------

def main():
    with open(INPUT_FILE, encoding="utf-8") as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    entries = bib_database.entries

    # Exclude honor thesis entries
    entries = [e for e in entries if not has_keyword(e, "honorthesis")]

    # Sections — featured can overlap with first_author/coauthor (appears in both)
    featured = [e for e in entries if has_keyword(e, "featured")]
    first_author = [e for e in entries if has_keyword(e, "1st")]
    invited = [e for e in entries if has_keyword(e, "invited")]
    coauthor = [
        e for e in entries
        if not has_keyword(e, "1st")
        and not has_keyword(e, "invited")
        and not has_keyword(e, "conference")
    ]

    # Sort newest-first for display in all sections
    featured.sort(key=get_year, reverse=True)
    first_author.sort(key=get_year, reverse=True)
    invited.sort(key=get_year, reverse=True)
    coauthor.sort(key=get_year, reverse=True)

    # Global numbering covers publications only (first_author + coauthor).
    # Invited talks are listed separately without numbers.
    # Oldest publication = [1], newest = [total].
    all_numbered = first_author + coauthor
    total = len(all_numbered)
    number_map = {e["ID"]: total - i for i, e in enumerate(all_numbered)}

    # Group coauthor by year
    coauthor_by_year = defaultdict(list)
    for e in coauthor:
        year_str = str(get_year(e))
        coauthor_by_year[year_str].append(e)

    sorted_years = sorted(
        coauthor_by_year.keys(),
        key=lambda y: int(y) if y.isdigit() else 0,
        reverse=True
    )

    # Write Markdown
    with open(OUTPUT_FILE, "w", encoding="utf-8") as md:
        md.write(FRONT_MATTER)

        # Featured: unnumbered — these papers also appear with numbers below
        if featured:
            md.write("## Featured Articles\n\n")
            for e in featured:
                md.write(f"- {format_entry(e)}\n")
            md.write("\n")

        # First Author: numbered
        md.write("## First Author Publications\n\n")
        for e in first_author:
            md.write(f"- **[{number_map[e['ID']]}]** {format_entry(e)}\n")
        md.write("\n")

        # Invited: unnumbered
        md.write("## Invited Talks and Seminars\n\n")
        for e in invited:
            md.write(f"- {format_entry(e)}\n")
        md.write("\n")

        # Co-Author: numbered, grouped by year
        md.write("## Co-Author Publications\n\n")
        for year in sorted_years:
            md.write(f"### {year}\n\n")
            for e in coauthor_by_year[year]:
                md.write(f"- **[{number_map[e['ID']]}]** {format_entry(e)}\n")
            md.write("\n")

    print(f"Markdown file written: {OUTPUT_FILE} ({total} numbered entries)")


if __name__ == "__main__":
    main()
