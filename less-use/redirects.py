import re

OLD_SITEMAP = "sitemap.xml"
OUTPUT_FILE = "_redirects"


def extract_urls(path):
    urls = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if "<loc>" in line:
                url = re.sub(r".*<loc>|</loc>.*", "", line).strip()
                if url.startswith("http"):
                    path_part = re.sub(r"https?://[^/]+", "", url)
                    urls.append(path_part)
    return urls


def convert_old_to_new(url):
    """
    Old formats:
      /semesters/subjects/papers/botany_dsc_101
      /semesters/subjects/papers/notes/botany_dsc_101_unit_2

    New formats:
      /notes/semester_1/botany/dsc_101
      /notes/semester_1/botany/dsc_101/unit_2
    """

    # Notes
    m_notes = re.match(
        r"^/semesters/subjects/papers/notes/([a-z_]+)_([a-z]+)_([0-9_]+)_unit_([0-9]+)$",
        url
    )
    if m_notes:
        subject, paper, code, unit = m_notes.groups()
        return f"/notes/semester_1/{subject}/{paper}_{code}/unit_{unit}"

    # Papers
    m_paper = re.match(
        r"^/semesters/subjects/papers/([a-z_]+)_([a-z]+)_([0-9]+)$",
        url
    )
    if m_paper:
        subject, paper, code = m_paper.groups()
        return f"/notes/semester_1/{subject}/{paper}_{code}"

    # Subjects
    m_sub = re.match(
        r"^/semesters/subjects/semester_1_([a-z_]+)$",
        url
    )
    if m_sub:
        subject = m_sub.group(1)
        return f"/notes/semester_1/{subject}"
    
    # Semester (rare case)
    sem = re.match(
        r"^/semesters/semester_([0-9]+)$",
        url
    )
    if sem:
        subject = m_sub.group(1)
        return f"/notes/semester_{sem}"
    

    return None


def is_academic(url):
    return (
        "/semesters/subjects/" in url
    )


# -----------------------------
# Main
# -----------------------------
old_urls = extract_urls(OLD_SITEMAP)

redirects = []

for old in old_urls:
    if is_academic(old):
        new = convert_old_to_new(old)
        if new:
            redirects.append(f"{old} {new} 301")
        else:
            print("No conversion rule matched:", old)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("\n".join(redirects))

print("✅ Redirects generated:", len(redirects))
print("✅ File saved as:", OUTPUT_FILE)