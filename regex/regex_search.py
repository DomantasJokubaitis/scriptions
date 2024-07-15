import re
import os

path = "text_files"

regex = re.compile(r"[^\s]+ič\s|[^\s]+iv\s|[^\s]+ij\s|[^\s]+ov\s|[^\s]+ev\s|[^\s]+ik\s", re.IGNORECASE)

files = os.listdir(path)

full_paths = []
surnames = []

for file in files:
    full_path = os.path.join(path, file)
    full_paths.append(full_path)


    
for full_path in full_paths:
    with open(full_path, "r", encoding="utf-8") as f:
        for line in f:
            surname = regex.search(line)
            if surname:
                surnames.append(surname.group())


for surname in surnames:
    print(surname)
    

