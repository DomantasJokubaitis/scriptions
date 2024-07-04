#! python3

import sys
import json
from pathlib import Path


path = Path("C:/Users/doman/Desktop/scriptions/password/data.json")

if path.exists():
    content = path.read_text()
    data = json.loads(content)

else:
    data = {}
    content = json.dumps(data)
    path.write_text(content)


def asking():
    want = str(input("Enter the application's name: "))
    retrieve_data(want)
    return want

def retrieve_data(want):
    content = path.read_text()
    data = json.loads(content)

    if want in data:
        for k1, v1 in data[want].items():
            print(f" {k1}: {v1} ")

    else:
        print("No account found. Would you like to add this account to the database? ")
        ans = input()
        new_data(ans, want)

def new_data(response, want):
    
    if response == "yes" or response == "y":
        mail = str(input("Enter the accounts mail: "))
        password = str(input("Enter the accounts password: "))
        infodict = {}
        infodict["mail"] = mail
        infodict["password"] = password
        data[want] = infodict
        content = json.dumps(data)
        path.write_text(content)
        print("Database updated! ")
        asking()
    if response == "no" or response == "n":
        print("Exiting...")
        sys.exit()

asking()

