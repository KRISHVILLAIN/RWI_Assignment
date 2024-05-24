# accept a number and display whether it is prime or not
num = int(input("Enter number:"))
i = 1
count = 0
while i <= num:
    if num % i == 0:
        count += 1
    i += 1
if count == 2:
    print(f"Entered {num} is Prime")
else:
    print(f"Entered {num} is Not Prime")
