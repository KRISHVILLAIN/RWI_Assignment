# write a function to accept a number and return its square using
# 	a) normal function
# 	b) lambda

def square_normal(num):
    return num ** 2


result = square_normal(5)
print("Square using normal function:", result)

square_lambda = lambda num: num ** 2

result = square_lambda(5)
print("Square using lambda function:", result)
