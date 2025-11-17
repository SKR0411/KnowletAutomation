import os

folder_path = "/storage/emulated/0/.hidden_files/workspace/web/knowlet_beta/notes/semester_1/"
count = 0

for filename in os.listdir(folder_path):
    if filename.endswith(".html"):
        name = filename[:-5]  # remove .html
        parts = name.split('_')

        # Only rename if there are at least 3 parts
        if len(parts) >= 3:
            new_parts = parts[2:]  # move last two parts to front
            new_name = "_".join(new_parts) + ".html"

            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} → {new_name}")
            count += 1

print(f"{count} files Renamed successfully")