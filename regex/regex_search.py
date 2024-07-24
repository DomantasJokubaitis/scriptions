import re
import os

path = "text_files"

regex = re.compile(r"\w+ič\b|\w+iv\b|\w+ij\b|\w+ov\b|\w+ev\b|\w+ik\b", re.IGNORECASE)

files = os.listdir(path)

full_paths, surnames = [], []

def find_surnames() -> list:
    for file in files:
        full_path = os.path.join(path, file)
        full_paths.append(full_path)
        
    for full_path in full_paths:
        with open(full_path, "r", encoding="utf-8") as f:
            for line in f:
                surname = regex.search(line)
                if surname:
                    surnames.append(surname.group())
    return surnames

def main():
    surnames = find_surnames()
    for surname in surnames:
        print(surname)

if __name__ == "__main__":
    main()

    
    

