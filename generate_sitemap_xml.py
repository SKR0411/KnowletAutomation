import os
from datetime import datetime

# === SETTINGS ===
BASE_URL = "https://knowlet.in"    # Change this to your site’s base URL
ROOT_DIR = "/storage/emulated/0/.hidden_workspace/web/knowlet"    # Folder where your HTML files are located
OUTPUT_FILE = ROOT_DIR + "/sitemap.xml"

# === FUNCTION TO GENERATE SITEMAP ===
def generate_sitemap():
    urls = []

    for root, _, files in os.walk(ROOT_DIR):
        for file in files:
            if file.endswith(".html"):
                path = os.path.join(root, file).replace("\\", "/")
                if "notes" in path:
                    url = BASE_URL + path.removeprefix(ROOT_DIR).removesuffix('.html')
                    lastmod = datetime.fromtimestamp(os.path.getmtime(os.path.join(root, file))).strftime("%Y-%m-%d")
                    urls.append((url, lastmod))
                    print('✔️' + url.removeprefix(BASE_URL))

    # Write sitemap.xml
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n\n')

        for url, lastmod in urls:
            f.write("    <url>\n")
            f.write(f"        <loc>{url}</loc>\n")
            f.write(f"        <lastmod>{lastmod}</lastmod>\n")
            f.write("    </url>\n")

        f.write("\n</urlset>")

    print(f"Sitemap created and successfully saved at: {OUTPUT_FILE}")
    print(f"Total URLs: {len(urls)}")

# === RUN ===
if __name__ == "__main__":
    generate_sitemap()