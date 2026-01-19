import os 

ROOT_DIR = "/sdcard/.workspace/web/knowlet/notes"

tag = '<div class="add-horizontal-scroll">'
count = 0
msg = ""
changed = 0
unchanged = 0
for root, _, files in os.walk(ROOT_DIR):
	for file in files:
		count += 1
		
		if file.endswith(".html"):
			
			file_path = os.path.join(root, file)
			with open(file_path, "r") as r:
				content = r.read()
			
			lines = content.splitlines()
			line_posn = 0
			new_content = ""
			msg = ""
			
			for line in lines:
				line_posn += 1
				new_line = ""
				
				if ("<table>" in line and tag + "<table>" not in line) or ("<pre>" in line and tag + "<pre>" not in line) :
					new_line = line.replace("<table>", tag + "<table>").replace("<pre>", tag + "<pre>")
					
				if ("</table>" in line and "</table></div>" not in line) or ("</pre>" in line and "</pre></div>" not in line) :
					new_line = line.replace("</table>", "</table></div>").replace("</pre>", "</pre></div>")
					
				if not new_line:
					new_line = line
				
				new_content += ("\n" if new_content else "") + new_line
			
			if new_content != content:
				with open(file_path, "w") as w:
					w.write(new_content)
				
				msg = "✔️"
				changed += 1 
				
			else:
				msg = "🟰"
				unchanged += 1
			
			print(msg + "  " + file_path.replace(ROOT_DIR, ""))
			
		
print("total: " + str(count))
print("changed: " + str(changed))
print("unchanged: " + str(unchanged))