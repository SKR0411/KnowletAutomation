import os
import re

# Folder path containing the HTML files
folder_path = "/sdcard/.workspace/web/knowlet/"

# Loop through all files in the folder
for filename in os.listdir(folder_path):
  if filename.endswith(".html"):
    # Match pattern: anything before unit_{number}, and ignore the rest
    match = re.match(r"^(.*unit_\d+)", filename)
    if match:
      new_name = match.group(1) + ".html"
      old_path = os.path.join(folder_path, filename)
      new_path = os.path.join(folder_path, new_name)
      
      # Rename file if name changes
      if old_path != new_path:
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} → {new_name}")