# define a function in such a way that it can accept n number of values and print their sum.
def sum_values(*args):
    
    total = sum(args)
    return total

# Example usage:
result = sum_values(10, 20, 30)
print("Sum:", result)  # Output: Sum: 60

result = sum_values(3.5, 7.2, 9.8, 2.1)
print("Sum:", result)  # Output: Sum: 22.6
