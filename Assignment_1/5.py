# accept marks from the user. Using if…….elif….  Else,  display whether result is  fail, pass, second class , first class, Distinction etc.
marks = float(input("Enter marks: "))


if marks < 0 or marks > 100:
    print("Invalid marks entered.")
elif marks < 40:
    print("Result: Fail")
elif marks < 60:
    print("Result: Pass")
elif marks < 75:
    print("Result: Second Class")
elif marks < 90:
    print("Result: First Class")
else:
    print("Result: Distinction")
