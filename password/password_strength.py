import re

regex1 = re.compile(r'\S{8,100}')
regex2 = re.compile(r'[a-z]')
regex3 = re.compile(r'[A-Z]')
regex4 = re.compile(r'[0-9]')

regexss = [regex1, regex2, regex3, regex4]


def check(password) -> bool:
    for regex in regexss:
        answer = regex.search(password)

        if answer == None:
            return True
        
        else:
            continue

    return False


def main():
    password_weak = True
    password = input("Enter your desired password: ")
    password_weak = check(password)
    
    if password_weak:
        print("Password is weak")
    else:
        print("Password is strong")
    

if __name__ == "__main__":
    main()


