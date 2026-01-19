import os
import re

# === SETTINGS ===
ROOT_DIR = "/sdcard/.workspace/web/Knowlet/notes/semester_1"  # Change if needed

# === REGEX PATTERN ===
# Removes everything between <head> and <meta charset="UTF-8">
pattern = re.compile(
  r'(<head>)([\s\S]*?)(<meta\s+charset=["\']UTF-8["\'])',
  re.IGNORECASE
)
y = 0
n = 0
# === PROCESS HTML FILES ===
for root, _, files in os.walk(ROOT_DIR):
  for filename in files:
    if re.match(r"unit_(\d+)\.html", filename):
      path = os.path.join(root, filename)
  
      with open(path, "r", encoding="utf-8") as f:
        content = f.read()
  
      # Replace everything between <head> and <meta charset="UTF-8">
      new_content = re.sub(pattern, r'\1\n    \3', content)
  
      if new_content != content:
        #with open(path, "w", encoding="utf-8") as f:
         # f.write(new_content)
        print(f"Cleaned header in: {path}")
        y += 1
      else:
        print(f"No change needed in: {path}")
        n += 1

print(f"✅ Done! All lines between <head> and <meta charset=\"UTF-8\"> removed.\nChanged: {y}\nUnchanged: {n}")