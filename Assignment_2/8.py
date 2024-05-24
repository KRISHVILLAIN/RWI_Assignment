# write a function to accept minimum 3 characters and maximum 5 characters.
# 	[ use default arguments method ]
def validate_input(input_str, min_length=3, max_length=5):
    
    if len(input_str) >= min_length and len(input_str) <= max_length:
        return True
    else:
        return False


# Example usage:
input_str = input("Enter a string: ")
if validate_input(input_str):
    print("Input is valid.")
else:
    print("Input is not valid. Please enter a string with length between 3 and 5 characters.")
