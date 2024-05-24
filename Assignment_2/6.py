# define a function which accepts a character and return toggle of it.
def toggle_character(char):
    # Check if the character is uppercase
    if char.isupper():
        # Convert uppercase to lowercase
        return char.lower()
    # Check if the character is lowercase
    elif char.islower():
        # Convert lowercase to uppercase
        return char.upper()
    else:
        # If the character is not a letter, return as is
        return char


# Example usage:
input_char = input("Enter a character: ")
toggled_char = toggle_character(input_char)
print("Toggled character:", toggled_char)
