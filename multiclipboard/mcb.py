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

def load_json() -> dict:
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

def ask_input() -> str:
    x = input("save/list/exit: ")
    return x


def main():

    text = pyperclip.paste()
    while True:
        wish = ask_input()

        if "save" in wish:
            wish = wish.removeprefix("save ")
            my_dict[wish] = text
            print(my_dict)
            store_json()

        elif "list" in wish:
            load_json()
            
        elif "exit" in wish:
            print("Exiting...")
            sys.exit()

        elif wish in my_dict.keys():
            pyperclip.copy(my_dict[wish])

        else:
            print("Function unavailable")

if __name__ == "__main__":
    main()






