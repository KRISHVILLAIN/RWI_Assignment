# accept a character and display whether it is upper case or lower case or not an alphabet.
char = input("Enter a character: ")

if char.isalpha():
    if char.isupper():
        print(f"The character '{char}' is uppercase.")
    else:
        print(f"The character '{char}' is lowercase.")
else:
    print(f"The character '{char}' is not an alphabet.")
