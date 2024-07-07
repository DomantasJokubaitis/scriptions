import re
import sys

answers = []

password = input("Enter your desired password: ")
regex1 = re.compile(r'\S{8,100}')
regex2 = re.compile(r'[a-z]')
regex3 = re.compile(r'[A-Z]')
regex4 = re.compile(r'[0-9]')

regexss = [regex1, regex2, regex3, regex4]

for regex in regexss:
    answer = regex.search(password)

    if answer == None:
        print("Password is weak")
        sys.exit()
    else:
        continue

print("Password strength: Strong")


