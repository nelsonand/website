import bibtexparser
from collections import defaultdict
import re
import sys

# Usage: python make_pubs.py [path/to/cv_prep.bib]
INPUT_FILE = sys.argv[1] if len(sys.argv) > 1 else "cv_prep.bib"
OUTPUT_FILE = "publications.md"

FRONT_MATTER = """---
layout: page
title: Publications
kicker: Publications
headline: Publications
subtitle: "{n_pubs} peer-reviewed and preprint publications ({n_first} as first author). Also on <a href='https://scholar.google.com/citations?user=_RET_uYAAAAJ'>Google Scholar</a> and <a href='https://orcid.org/0000-0002-9612-1936'>ORCID</a>. Invited talks and conference contributions are on the <a href='/conferences/'>Talks</a> page."
---

"""

# Selected publications, in display order. Keep in sync with the
# "Selected Design and Engineering Publications" list in the CV (main.tex).
SELECTED_KEYS = [
    "nelson_pedestal_2026",
    "slendebroek_exploring_2026",
    "cohen_yinsen_2026",
    "thecentaurcollaboration_compact_2026",
    "themantacollaboration_manta_2024",
    "salm_poloidal_2026",
    "guizzo_electromagnetic_2025",
    "nelson_implications_2024",
    "miller_power_2024",
    "jalalvand_multimodal_2025",
    "nelson_robust_2023",
]

# Temporary corrections for known errors in the Zotero data. Remove each one
# once it has been fixed in Zotero and the bib has been re-exported.
DATA_FIXES = {
    # "M. Curie" duplicates "Max Curie" in the author list
    "jalalvand_multimodal_2025": {"author": lambda a: a.replace(" and Curie, M. and ", " and ")},
    # DOI field holds an unrelated OSTI DOI; the url field has the correct one
    "bechtelamara_accelerating_2025": {"doi": lambda d: "10.3389/fphy.2024.1524041",
                                        "journaltitle": lambda j: "Frontiers in Physics"},
}


# ----------------------------
# Helpers
# ----------------------------

# LaTeX accent commands that appear in the Zotero export, e.g. {\\v{c}} -> č
LATEX_ACCENTS = {"v": "\u030c", "'": "\u0301", "`": "\u0300", '"': "\u0308",
                 "^": "\u0302", "~": "\u0303", "c": "\u0327", "u": "\u0306"}


def latex_to_unicode(text):
    import unicodedata

    def repl(m):
        return unicodedata.normalize("NFC", m.group(2) + LATEX_ACCENTS[m.group(1)])

    return re.sub(r"\\([v'`\"^~cu])\s*\{?([A-Za-z])\}?", repl, text)


# Inline math that appears in titles
LATEX_MATH = {r"$\beta$": "β", r"$\times$": "×", r"$\alpha$": "α", r"$\delta$": "δ"}


def clean(text):
    if not text:
        return ""
    for k, v in LATEX_MATH.items():
        text = text.replace(k, v)
    return re.sub(r"[{}]", "", latex_to_unicode(text)).strip()


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
    name = re.sub(r"[{}]", "", latex_to_unicode(name))
    if re.search(r"\b(A\.?\s*O\.?|Oak|Andrew\s+Oakleigh)\s+Nelson\b", name, re.IGNORECASE):
        name = f"**{name}**"
    return name


def format_authors(author_field):
    authors = [a.strip() for a in author_field.split(" and ")]
    # Drop exact duplicate names (a known Zotero export glitch)
    seen = set()
    authors = [a for a in authors if not (a in seen or seen.add(a))]

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
        if re.search(r"\b(A\.?\s*O\.?|Oak|Andrew\s+Oakleigh)\s+Nelson\b", name, re.IGNORECASE):
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

    if venue or volume or pages:
        citation += "."

    # Some Zotero entries store the DOI as a full URL
    doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi.strip())
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
    for e in entries:
        for field, fix in DATA_FIXES.get(e["ID"], {}).items():
            e[field] = fix(e.get(field, ""))

    # Exclude honor thesis entries
    entries = [e for e in entries if not has_keyword(e, "honorthesis")]

    # Sections. Selected papers also appear (numbered) in the lists below.
    # Filters match the CV: conference abstracts and invited talks are not
    # numbered publications; they live on the Talks page (conferences.md).
    by_key = {e["ID"]: e for e in entries}
    missing = [k for k in SELECTED_KEYS if k not in by_key]
    if missing:
        print(f"Warning: selected keys not found in bib: {missing}")
    featured = [by_key[k] for k in SELECTED_KEYS if k in by_key]
    first_author = [
        e for e in entries
        if has_keyword(e, "1st")
        and not has_keyword(e, "conference")
        and not has_keyword(e, "invited")
    ]
    coauthor = [
        e for e in entries
        if not has_keyword(e, "1st")
        and not has_keyword(e, "invited")
        and not has_keyword(e, "conference")
    ]

    # Sort newest-first for display in all sections
    first_author.sort(key=get_year, reverse=True)
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
        md.write(FRONT_MATTER.format(n_pubs=total, n_first=len(first_author)))

        # Selected: unnumbered — these papers also appear with numbers below
        if featured:
            md.write("## Selected Design and Engineering Publications\n\n")
            for e in featured:
                md.write(f"- {format_entry(e)}\n")
            md.write("\n")

        # First Author: numbered
        md.write("## First Author Publications\n\n")
        for e in first_author:
            md.write(f"- **[{number_map[e['ID']]}]** {format_entry(e)}\n")
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
