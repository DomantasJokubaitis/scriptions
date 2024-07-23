import re, os
from pathlib import Path


path = Path("am_eu_date_regex")
file_paths = os.listdir(path)
matches = []


regex = re.compile(r"\d{2}-\d{2}-\d{4}")
for item in file_paths:
    answer = regex.search(item)
    if answer:
        print(answer.group())

# testing