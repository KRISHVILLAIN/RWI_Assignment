# using switch ….case   display whether accepted character is vowel or not.
character = input("Enter a character: ")

match character:
    case 'a':
        print(f"{character} is a vowel.")
    case 'e':
        print(f"{character} is a vowel.")
    case 'i':
        print(f"{character} is a vowel.")
    case 'o':
        print(f"{character} is a vowel.")
    case 'u':
        print(f"{character} is a vowel.")
    case _:
        print(f"{character} is not a vowel.")
