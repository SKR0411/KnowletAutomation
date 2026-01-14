import os

rdp = "/storage/emulated/0/Workspace /.hidden_workspace/web/Knowlet_beta/semesters/subjects/papers"
nrdp =  "/storage/emulated/0/Workspace /.hidden_workspace/web/Knowlet_beta/notes"

def get_semester(course_number):
  """Determine semester based on course code number."""
  num = int(course_number)
  if 100 <= num < 150:
    return "semester_1"
  elif 150 <= num < 200:
    return "semester_2"
  elif 200 <= num < 250:
    return "semester_3"
  elif 250 <= num < 300:
    return "semester_4"
  elif 300 <= num < 350:
    return "semester_5"
  elif 350 <= num < 400:
    return "semester_6"
  elif 400 <= num < 550:
    return "semester_7"
  elif 550 <= num < 600:
    return "semester_8"
  else:
    return "semester_0"


for fn in os.listdir(rdp):
  
	if fn.endswith('.html'):
		
		fp = os.path.join(rdp, fn)
		parts = fn.split('.')
		parts = parts[0].split("_")
		
		if len(parts) == 4 :
		  sem = get_semester(parts[3])
		  nfp = nrdp + "/" + sem + "/" + parts[0] + "_" + parts[1] + "/" + parts[2] + "_" + parts[3] + ".html"
		  #ndp = nrdp + "/" + sem + "/" + parts[0] + "_" + parts[1] + "/" + parts[2] + "_" + parts[3]
		else:
		  sem = get_semester(parts[2])
		  nfp = nrdp + "/" + sem + "/" + parts[0] + "/" + parts[1] + "_" + parts[2] + ".html"
		  #ndp = nrdp + "/" + sem + "/" + parts[0] + "/" + parts[1] + "_" + parts[2]
			
		print(nfp)
			
		with open(fp, 'r', encoding='utf-8') as file:
			content = file.read()
		
		#os.makedirs(ndp, exist_ok=True)
    
		#with open(nfp, 'w', encoding="utf-8") as file:
			#file.write(content)
		
print("\n\nNested folders and files created successfully")