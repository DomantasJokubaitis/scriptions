import array as arr

numbers = arr.array("i", [])


def adding():
    try:
        number_a = int(input("Enter an integer to add: "))
        numbers.append(number_a)
        menu()
    except ValueError:
        print("Input isn't a whole number!")
        menu()

def removing():
    if numbers:
        number_r = int(input("Enter a number to remove: "))
        if number_r in numbers:
            i = numbers.index(number_r)
            popped = numbers.pop(i)
            print(f"Number {popped} was removed")
            menu()
        else:
            print("Number isn't in the array")
            menu()
    else:
        print("Array is empty")
        menu()

def showing():

    if numbers:
        print(f"Array contains these numbers: ")
        for element in numbers:
            print(element, end="  ")
        menu()
    else:
        print("Array is empty! ")
        menu()

def menu():
    try:
        choice = int(input("\n1 - Add new element/ 2 - Remove element / 3 - Show all elements: "))
    except ValueError:
        print("Invalid command! ")
        menu()
    while choice < 1 or choice > 3:
        print("Invalid command! ")
        menu()
    match choice:
        case 1:
            adding()
        case 2:
            removing()
        case 3:
            showing()

menu()

