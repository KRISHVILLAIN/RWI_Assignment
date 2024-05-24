# define a function which accepts character,int,string and display them.
def display_info(char, integer, string):
    print("Character:", char)
    print("Integer:", integer)
    print("String:", string)


char_input = input("Enter a character: ")
integer_input = int(input("Enter an integer: "))
string_input = input("Enter a string: ")

display_info(char_input, integer_input, string_input)
