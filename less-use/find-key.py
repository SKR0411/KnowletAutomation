import os 

ROOT_DIR = "/sdcard/.workspace/web//knowlet"
SUPABASE_URL = "https://ampwczxrfpbqlkuawrdf.supabase.co";
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFtcHdjenhyZnBicWxrdWF3cmRmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjI3OTk4MzYsImV4cCI6MjA3ODM3NTgzNn0.hFib9Y5x02b5VWjKuNi1XkUYvycmrp0DQhnwNkOGJEU";

count = 0
exist = 0

for root, _, files in os.walk(ROOT_DIR):
	for file in files:
		
		if file.endswith(".js") or file.endswith(".html"):
		
			count += 1
			
			file_path = os.path.join(root, file)
			
			with open(file_path, "r") as r:
				content = r.read()
			
			if SUPABASE_KEY in content:
				exist += 1
				print(file_path.replace(ROOT_DIR, ""))
		
print("total: " + str(count))
print("exist: " + str(exist))