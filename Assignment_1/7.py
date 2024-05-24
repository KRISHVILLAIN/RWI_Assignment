# accept numbers till user enters 0 and display the total of all the numbers entered.
total = 0

while True:
    number = float(input("Enter a number (enter 0 to stop): "))

    if number == 0:
        break

    total += number

print(f"Total of all numbers entered: {total}")
