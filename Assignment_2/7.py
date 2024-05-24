# define a function which accepts a string , toggle and return it.
# 	[ hint :  use "swapcase()" function of string ]

def toggle_string(input_string):
    # Use swapcase() to toggle the case of each character in the string
    return input_string.swapcase()


input_str = input("Enter a string: ")
toggled_str = toggle_string(input_str)
print("Toggled string:", toggled_str)

