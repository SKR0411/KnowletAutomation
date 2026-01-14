import os
import re

BASE_DIR = "/storage/emulated/0/Workspace /.hidden_workspace/web/Knowlet/notes/semester_1"  # Folder containing all your HTML files
sf = 0
uf = 0
nf = 0

def generate_meta_description(title, toc_items):
  if toc_items:
    toc_summary = ", ".join(toc_items[:6])
    return (f"Comprehensive notes for {title}. Covers key topics such as {toc_summary}. "
        f"Includes definitions, explanations, and short summaries for college students.")
  else:
    return (f"Comprehensive notes for {title}. Includes key concepts, definitions, "
        f"and summaries for college students.")

def generate_meta_keywords(title, toc_items):
  title_keywords = re.sub(r"[^a-zA-Z0-9 ]", "", title).split()
  keywords = set(word.lower() for word in title_keywords if len(word) > 2)
  if toc_items:
    for topic in toc_items:
      for word in re.sub(r"[^a-zA-Z0-9 ]", "", topic).split():
        if len(word) > 2:
          keywords.add(word.lower())
  return ", ".join(sorted(keywords))

def extract_title(html):
  m = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
  return m.group(1).strip() if m else "this page"

def extract_toc_items(html):
  toc_match = re.search(r'<div[^>]id=["\']toc["\'][^>]>(.*?)</div>', html, re.DOTALL | re.IGNORECASE)
  if not toc_match:
    return []
  toc_html = toc_match.group(1)
  items = re.findall(r"<a[^>]>(.*?)</a>", toc_html, re.DOTALL | re.IGNORECASE)
  return [re.sub(r"\s+", " ", i.strip()) for i in items if i.strip()]

def insert_meta_tag(html, meta_tag):
  head_match = re.search(r'<meta name="viewport" content="width=device-width, initial-scale=1.0">', html, re.IGNORECASE)
  if not head_match:
    return html  # skip if <head> missing

  insert_pos = head_match.end()
  return html[:insert_pos] + "\n" + meta_tag + html[insert_pos:]

for root, _, files in os.walk(BASE_DIR):
  for file in files:
    #if not file.endswith(".html"):
     # continue
    
    if re.match(r"unit_(\d+)\.html", file):
      path = os.path.join(root, file)
      sf += 1
      
      with open(path, "r", encoding="utf-8") as f:
        html = f.read()
  
      title = extract_title(html)
      toc_items = extract_toc_items(html)
  
      # Generate new meta content
      new_desc = generate_meta_description(title, toc_items)
      new_keys = generate_meta_keywords(title, toc_items)
  
      # === Description ===
      desc_match = re.search(
        r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']+)["\']',
        html, re.IGNORECASE | re.DOTALL
      )
      if desc_match:
        old_desc = desc_match.group(1).strip()
        if old_desc != new_desc:
          html = re.sub(
            r'<meta[^>]+name=["\']description["\'][^>]*>',
            f'  <meta name="description" content="{new_desc}">',
            html, flags=re.IGNORECASE
          )
          print(f"↻ Updated description in {file}")
          uf += 1
      else:
        html = insert_meta_tag(html, f'    <meta name="description" content="{new_desc}">')
        print(f"✓ Added description in {file}")
        nf += 1
  
      # === Keywords ===
      keys_match = re.search(
        r'<meta[^>]+name=["\']keywords["\'][^>]+content=["\'](.*?)["\']',
        html, re.IGNORECASE | re.DOTALL
      )
      if keys_match:
        old_keys = keys_match.group(1).strip()
        if old_keys != new_keys:
          html = re.sub(
            r'<meta[^>]+name=["\']keywords["\'][^>]*>',
            f'  <meta name="keywords" content="{new_keys}">',
            html, flags=re.IGNORECASE
          )
          print(f"↻ Updated keywords in {file}")
      else:
        html = insert_meta_tag(html, f'    <meta name="keywords" content="{new_keys}">')
        print(f"✓ Added keywords in {file}")
      
      #with open(path, "w", encoding="utf-8") as f:
      #  f.write(html)
      

print(f'Scaned = {sf}\nUpdated = {uf}\nNew = {nf}')
