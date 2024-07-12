import json
from pathlib import Path
import sys

path = Path("chatgptexer\\r_w_json\\data.json")

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
    
    
def modifying():
    contents = loading()
    if contents == None:
        return []
    change_person = input("Enter the person's name to modify: ")

    for dictionary in contents:

        if dictionary["name"] == change_person:
            change = input("What info would you like to modify? ")
            if "mail" in change and "age" in change:
                email = input("Enter an email address: ")
                age = int(input("Enter age: "))
                dictionary["age"], dictionary["email"] = age, email
                break
            elif "mail" in change:
                email = input("Enter an email address: ")
                dictionary["email"] = email
                break
            elif "age" in change:
                age = int(input("Enter age: "))
                dictionary["age"] = age
                break
            else:
                print("Invalid answer")
                break

        else:
            continue
    

def main():
    contents = loading()

    if contents == None:
        contents = []
        
    new_dict = {}
    commands = ("add", "search", "modify", "delete", "exit")
    wish = input("Add | Search | Modify | Delete | Exit : ").lower()
    while wish not in commands:
        wish = input("Unknown command, try again: ")
    if "add" in wish:
        name = str(input("Enter a name: "))
        age = int(input("Enter age: "))
        email = input("Enter an email address: ")

        while "@" not in email:
            email = input("Invalid email, try again: ")

        new_dict["name"], new_dict["age"], new_dict["email"] = name, age, email
        contents.append(new_dict)

    elif "modify" in wish:
       modifying()

    elif wish == "search":
        name = input("Enter name for lookup: ")
        for dictionary in contents:
            if dictionary["name"] == name:
                for value in dictionary.values():
                    print(value)
            else:
                continue

    elif wish == "delete":
        name = input("Enter name to delete: ")
        for dictionary in contents:
            if dictionary["name"] == name:
                index = contents.index(dictionary)
                del contents[index]
                print("Data succesfully deleted!")
            else:
                continue
    elif wish == "exit":
        sys.exit()
            

    
    new_text = json.dumps(contents)
    path.write_text(new_text)

if __name__ == "__main__":
    main()

#implement search function by name
#implement delete function by name
#implement detail update function 

