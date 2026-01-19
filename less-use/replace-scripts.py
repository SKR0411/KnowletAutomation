import os 

ROOT_DIR = "/sdcard/.workspace/web/knowlet/notes"
count = 0
for root, _, files in os.walk(ROOT_DIR):
	for file in files:
		
		if file.endswith(".html"):
			
			file_path = os.path.join(root, file)
			with open(file_path, "r") as r:
				content = r.read()
			if '''<script src="../../../../assets/scripts/supabase.js"></script>''' in content and '''<script src="../../../../assets/scripts/units.js"></script>''' in content:
				content = content.replace('''<script src="../../../../assets/scripts/units.js"></script>''',
'').replace('''<script src="../../../../assets/scripts/supabase.js"></script>''',
'''<script src="../../../../assets/scripts/units.js"></script>''')

				with open(file_path, "w") as w:
					w.write(content)

				print(file_path.replace(ROOT_DIR, ""))
				count += 1

print("total: {}".format(count))