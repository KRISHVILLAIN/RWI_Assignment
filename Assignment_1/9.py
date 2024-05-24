# display fibonicii series of 10 numbers
a, b = 1, 1
i = 3
print(a,b,end=",")
while i <= 10:
    n = a + b
    a = b
    b = n
    print(n,end=",")
    i += 1
