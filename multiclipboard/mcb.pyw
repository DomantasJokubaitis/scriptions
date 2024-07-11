import json
from pathlib import Path
import pyperclip
import os
import sys

path = Path("multiclipboard\\jason.json")
if not path.exists():
    os.makedirs("multiclipboard\\")
    my_dict = {}
if path.exists():
    content = path.read_text()
    my_dict = json.loads(content)

def load_json():
    content = path.read_text()
    my_dict = json.loads(content)
    x = ', '
    y = x.join(my_dict)
    pyperclip.copy(y)

def store_json():
    contents = json.dumps(my_dict)
    path.write_text(contents)

def ask_input():
    x = input("Enter: ")
    return x



text = pyperclip.paste()
wish = ask_input()

while True:

    if "save" in wish:
        wish = wish.removeprefix("save ")
        my_dict[wish] = text
        print(my_dict)
        store_json()
        wish = ask_input()

    elif "list" in wish:
        load_json()
        wish = ask_input()
        

    elif "exit" in wish:
        print("Exiting...")
        sys.exit()

    elif wish in my_dict.keys():
        pyperclip.copy(my_dict[wish])
        wish = ask_input()

    else:
        print("Function unavailable")
        wish = ask_input()






