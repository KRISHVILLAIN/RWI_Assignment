# write a function with 2 arguments , second argument should be "default argument" and display them. Using
# 	a) normal function
# 	b) lambda

def display_arguments_normal(arg1, arg2="default"):
    print("Argument 1:", arg1)
    print("Argument 2:", arg2)

# Example usage:
display_arguments_normal("Value 1")

display_arguments_lambda = lambda arg1, arg2="default": print("Argument 1:", arg1, "\nArgument 2:", arg2)

# Example usage:
display_arguments_lambda("Value 1")
