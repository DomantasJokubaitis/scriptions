import pyperclip
import re

text = pyperclip.paste()

regex = re.compile(r'\S+@\S+|\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}')
answer = regex.findall(text)

if not answer:
    print("Nothing found.")

for i in answer:
    print(i)