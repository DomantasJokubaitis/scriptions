import json
from pathlib import Path
import pyperclip
import os
import sys

path = Path("multiclipboard\\jason.json")

if not path.parent.exists():
    os.makedirs("multiclipboard\\")
if not path.exists():
    my_dict = {}
else:
    try:
        content = path.read_text()
        my_dict = json.loads(content)
    except json.JSONDecodeError:
        my_dict = {}

def load_json():
    try:
        content = path.read_text()
        my_dict = json.loads(content)
        copied = ",".join(my_dict.keys())
        pyperclip.copy(copied)
    except json.JSONDecodeError:
        return {}

def store_json():
    contents = json.dumps(my_dict)
    path.write_text(contents)

def ask_input():
    x = input("save/list/exit: ")
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






