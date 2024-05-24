# display prime numbers from 3 to 30
i = 3
while i <= 30:
    count = 0
    j = 1
    while j <= i:
        if i % j == 0:
            count += 1
        j += 1
    if count == 2:
        print(i)
    i += 1
