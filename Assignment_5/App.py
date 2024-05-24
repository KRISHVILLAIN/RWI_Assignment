from spcial import Arithmetic, display

# Invoke functions from Arithmetic module
result_add = Arithmetic.add(5, 3)
result_multiply = Arithmetic.multiply(5, 3)
result_subtract = Arithmetic.subtract(5, 3)

print("Addition:", result_add)
print("Multiplication:", result_multiply)
print("Subtraction:", result_subtract)

# Invoke function from Display module
message = display.wish("Alice")
print(message)
