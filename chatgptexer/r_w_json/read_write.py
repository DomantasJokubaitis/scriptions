import json
from pathlib import Path
import sys
import re

path = Path("chatgptexer\\r_w_json\\data.json")

regex = re.compile(r"[\w.]+@[\w.]+")

def loading():
    if path.exists():
        try:
            read = path.read_text()
            contents = json.loads(read)
            return contents
        except FileNotFoundError:
            print("File not found. ")
            return []
        except json.JSONDecodeError:
            print("Decoding failed. ")
            return []
    if not path.exists():
        print("Path doesn't exist!")
        return []
    
def new_email_address():
    while True:
        email = input("Enter a new email address: ")

        if regex.search(email):
            return email
        else:
            continue


def new_age():
    while True:
        age = int(input("Enter a new age: "))
        if 0 < age < 120:
            return age     
        else:
            continue

    
    
def modifying():
    contents = loading()
    if contents == None:
        return []
    change_person = input("Enter the person's name to modify: ")
    person_found = False

    for dictionary in contents:

        if dictionary["name"] == change_person:
            person_found = True
            change = input("What info would you like to modify? ")
            if "mail" in change and "age" in change:
                email = new_email_address()
                age = new_age()
                dictionary["age"], dictionary["email"] = age, email
                break
            elif "mail" in change:
                email = new_email_address
                dictionary["email"] = email
                break
            elif "age" in change:
                age = new_age()
                dictionary["age"] = age
                break
            else:
                print("mail/age: ")
                break

        else:
            continue

    if person_found == False:
        print("Person was not found. ")

    
def main():
    
    contents = loading()
    if contents == None:
        contents = []

    while True:
        
        new_dict = {}
        commands = ("add", "search", "modify", "delete", "exit")
        wish = input("Add | Search | Modify | Delete | Exit : ").lower()
        while wish not in commands:
            wish = input("Unknown command, try again: ")

        if "add" in wish:
            name = str(input("Enter a name: "))
            age = new_age()
            email = new_email_address()
                
            new_dict["name"], new_dict["age"], new_dict["email"] = name, age, email
            contents.append(new_dict)

        elif "modify" in wish:
            modifying()

        elif wish == "search":
            person_found = False
            name = input("Enter name for lookup: ")
            for dictionary in contents:
                if dictionary["name"] == name:
                    person_found = True
                    for value in dictionary.values():
                        print(value)
                    break
                else:
                    continue
            if person_found == False:
                print("Person was not found. ")

        elif wish == "delete":
            name = input("Enter name to delete: ")
            person_found = False
            for dictionary in contents:
                if dictionary["name"] == name:
                    index = contents.index(dictionary)
                    del contents[index]
                    print("Data succesfully deleted!")
                    person_found = True
                else:
                    continue
            if person_found == False:
                print("Person was not found")
        elif wish == "exit":
            sys.exit()
            
    
        new_text = json.dumps(contents)
        path.write_text(new_text)

if __name__ == "__main__":
    main()
