import os
import re

# ---------------------------
# Templates
# ---------------------------

paptem = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Subject] [Paper] – Knowlet</title>
  <link rel="stylesheet" href="../../../assets/styles/papers.css">
  <link rel="icon" href="https://knowlet.netlify.app/assets/knowlet_icon_round.png" type="image/x-icon">
</head>
<body>
  <header class="header">
  <h1>[Subject] [Paper]</h1>
  <p>Select a unit to view notes and study materials</p>
  </header>

  <main class="main">
  <section class="subjects-section">
    <h2>Units</h2>
    <div class="subjects-grid"></div>
  </section>
  </main>

  <footer class="footer">
  <p>© 2025 Knowlet | All rights reserved</p>
  </footer>
  <script src="../../../assets/scripts/papers.js"></script>
</body>
</html>
'''

subtem = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Semester] [Subject] – Knowlet</title>
  <link rel="stylesheet" href="../../assets/styles/subjects.css">
  <link rel="icon" href="https://knowlet.netlify.app/assets/knowlet_icon_round.png" type="image/x-icon">
</head>
<body>
  <header class="header">
  <h1>[Semester] [Subject]</h1>
  <p>Select a paper to continue</p>
  </header>

  <main class="main">
  <section class="subjects-section">
    <h2>Papers</h2>
    <div class="subjects-grid"></div>
  </section>
  </main>

  <footer class="footer">
  <p>© 2025 Knowlet | All rights reserved</p>
  </footer>
  <script src="../../assets/scripts/subjects.js"></script>
</body>
</html>
'''

semtem = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Semester] – Knowlet</title>
  <link rel="stylesheet" href="../assets/styles/semesters.css">
  <link rel="icon" href="https://knowlet.netlify.app/assets/knowlet_icon_round.png" type="image/x-icon">
</head>
<body>
  <header class="header">
  <h1>[Semester]</h1>
  <p>Select a subject to continue</p>
  </header>

  <main class="main">
  <section class="subjects-section">
    <h2>Subjects</h2>
    <div class="subjects-grid"></div>
  </section>
  </main>

  <footer class="footer">
  <p>© 2025 Knowlet | All rights reserved</p>
  </footer>
  <script src="../assets/scripts/semesters.js"></script>
</body>
</html>
'''

# ---------------------------
# Paths & Patterns
# ---------------------------

root_dir = "/storage/emulated/0/.hidden_files/workspace/web/knowlet/notes"
unit_pattern = re.compile(r"unit_(\d+)\.html")

# ---------------------------
# Hierarchy data structure
# ---------------------------
# {
#   "semester_1": {
#     "economics": {
#       "idc_101": ["unit_1.html", "unit_2.html"]
#     }
#   }
# }
# ---------------------------

structure = {}
semcount = [0, 0, 0, 0]
subcount = [0, 0, 0, 0]
papcount = [0, 0, 0, 0]
status = ''


def write(out_path, html):
  if os.path.exists(out_path):
    with open(out_path, "r") as r:
      c = r.read()
    if c != html:
      with open(out_path, "w") as f:
        f.write(html)
      status = '✔️'
    else:
      status = '🟰'
  else:
    with open(out_path, "w") as f:
      f.write(html)
    status = '➕'
  print(out_path.removeprefix(root_dir).replace('.html', ''), status)
  return status

def count(status, s):
  s[0] += 1
  if status == '➕':
    s[1] += 1 
  elif status == '🟰':
    s[2] += 1 
  elif status == '✔️':
    s[3] += 1
  
  
# ---------------------------
# Step 1: Build hierarchy
# ---------------------------

for semester in os.listdir(root_dir):
  sem_path = os.path.join(root_dir, semester)
  if not os.path.isdir(sem_path):
    continue

  structure[semester] = {}

  for subject in os.listdir(sem_path):
    sub_path = os.path.join(sem_path, subject)
    if not os.path.isdir(sub_path):
      continue

    structure[semester][subject] = {}

    for paper in os.listdir(sub_path):
      pap_path = os.path.join(sub_path, paper)
      if not os.path.isdir(pap_path):
        continue

      units = []
      for file in os.listdir(pap_path):
        if unit_pattern.match(file):
          units.append(file)

      units.sort()
      structure[semester][subject][paper] = units

# ---------------------------
# Step 2: Generate HTML pages
# ---------------------------

# 2A. Generate Paper Pages (Units)
for sem, subjects in structure.items():
  for sub, papers in subjects.items():
    for pap, units in papers.items():

      tags = ""
      for u in units:
        unit_name = u.replace(".html", "").replace("_", " ").title()
        tags += f'\n      <div class="subject-card"><a href="{pap}/{u}">{unit_name}</a></div>'

      html = paptem.replace(
        '<div class="subjects-grid"></div>',
        '<div class="subjects-grid">' + tags + '\n    </div>'
      )
      html = html.replace("[Subject]", sub.replace("_", " ").title())
      html = html.replace("[Paper]", pap.replace("_", " ").upper())

      out_path = os.path.join(root_dir, sem, sub, pap + ".html")
      status = write(out_path, html)
      count(status, papcount)
      
# 2B. Generate Subject Pages (Papers)
for sem, subjects in structure.items():
  for sub, papers in subjects.items():

    tags = ""
    for pap in papers.keys():
      pap_title = pap.replace("_", " ").upper()
      tags += f'      <div class="subject-card"><a href="{sub}/{pap}.html">{pap_title}</a></div>\n'

    html = subtem.replace(
      '<div class="subjects-grid"></div>',
      '<div class="subjects-grid">\n' + tags + '    </div>'
    )
    html = html.replace("[Semester]", sem.replace("_", " ").title())
    html = html.replace("[Subject]", sub.replace("_", " ").title())

    out_path = os.path.join(root_dir, sem, sub + ".html")
    status = write(out_path, html)
    count(status, subcount)
    
# 2C. Generate Semester Pages (Subjects)
for sem, subjects in structure.items():

  tags = ""
  for sub in subjects.keys():
    sub_title = sub.replace("_", " ").title()
    tags += f'      <div class="subject-card"><a href="{sem}/{sub}.html">{sub_title}</a></div>\n'

  html = semtem.replace(
    '<div class="subjects-grid"></div>',
    '<div class="subjects-grid">\n' + tags + '    </div>'
  )
  html = html.replace("[Semester]", sem.replace("_", " ").title())

  out_path = os.path.join(root_dir, sem + ".html")
  status = write(out_path, html)
  count(status, semcount)
  
print('\nSemester: [Total, New, Same, Changed] =', semcount)
print('Subject:  [Total, New, Same, Changed] =', subcount)
print('Paper:    [Total, New, Same, Changed] =', papcount)
print("HTML generation complete.")