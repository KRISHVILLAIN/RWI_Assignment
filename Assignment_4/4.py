# write a function with variable no. of arguments and display them. Using
# 	a) normal function
# 	b) lambda

def display_arguments_normal(*args):
    print("Arguments:")
    for arg in args:
        print(arg)


# Example usage:
display_arguments_normal("arg1", "arg2", "arg3")

display_arguments_lambda = lambda *args: [print(arg) for arg in args]

# Example usage:
display_arguments_lambda("arg1", "arg2", "arg3")
