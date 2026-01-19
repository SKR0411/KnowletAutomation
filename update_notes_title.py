import os
import re

FOLDER_PATH = "/storage/emulated/0/.hidden_workspace/web/knowlet/notes"  # Change this to your folder containing HTML files

def get_semester(course_number):
  """Determine semester based on course code number."""
  num = int(course_number)
  if 100 <= num < 150:
    return "1st Semester"
  elif 150 <= num < 200:
    return "2nd Semester"
  elif 200 <= num < 250:
    return "3rd Semester"
  elif 250 <= num < 300:
    return "4th Semester"
  elif 300 <= num < 350:
    return "5th Semester"
  elif 350 <= num < 400:
    return "6th Semester"
  elif 400 <= num < 550:
    return "7th Semester"
  elif 550 <= num < 600:
    return "8th Semester"
  else:
    return "Any Semester"

def generate_title(path):
  name = path.removeprefix(FOLDER_PATH).removesuffix('.html')
  parts = name.split("/")
  #print(parts)
  sem = ' '.join(parts[1].split('_')).capitalize()
  sub = ' '.join(w.capitalize() for w in (parts[2].split('_')))
  paper = ' '.join(parts[3].split('_')).upper()
  unit = ' '.join(parts[4].split('_')).capitalize()
  
  semester = get_semester(int((parts[3].split('_'))[1]))
  
  return f"{sub} {paper} {unit} | {semester} Notes - Knowlet"
  
# Regex to find <title> tag
title_pattern = re.compile(r'<title>.*?</title>', re.IGNORECASE)

Changed = 0
Total = 0
CL = []

for root, _, files in os.walk(FOLDER_PATH):
  for filename in files:
    if re.match(r"unit_(\d+)\.html", filename):
      file_path = os.path.join(root, filename)
      Total += 1
      
      with open(file_path, "r", encoding="utf-8") as f:
        c = f.read()
      
      new_title = generate_title(file_path)
      #print(new_title)
      if title_pattern.search(c):
        # Replace existing title
        nc = title_pattern.sub(f"<title>{new_title}</title>", c)
      else:
        # Insert <title> inside <head> if missing
        nc = re.sub(r"(<head.*?>)", r"\1\n<title>" + new_title + "</title>", c, flags=re.IGNORECASE)
      
      if c != nc:
        Changed += 1
        with open(file_path, "w", encoding="utf-8") as f:
          f.write(nc)
        print(f'{file_path.removeprefix(FOLDER_PATH)} ✅')
      else:
        print(f'{file_path.removeprefix(FOLDER_PATH)} 🟰')
        
print(f"All titles updated successfully!\nTotal: {Total}\nChanged: {Changed}")