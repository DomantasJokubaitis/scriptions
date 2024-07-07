import pyperclip
import re

text = pyperclip.paste()

regex = re.compile(r'\S{0,30}?@\S{0,30}|\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}|\+\d{3}\s\d{3}\s\d{2}\s\d{3}')
answer = regex.findall(text)

if not answer:
    print("Nothing found.")

for i in answer:
    print(i)