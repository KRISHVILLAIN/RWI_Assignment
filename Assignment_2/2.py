# define a function which accepts a number and return its square.
def square(number):
    return number ** 2


num = float(input("Enter a number: "))
result = square(num)
print("The square of", num, "is", result)
