# define nested function and show how will you invoke it.

def outer_function():
    print("This is outer function")

    def inner_function():
        print("This is inner function")

    # Call the inner function
    inner_function()

# Call the outer function
outer_function()
