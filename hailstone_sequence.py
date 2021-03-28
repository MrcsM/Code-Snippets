n = int(input("Enter a number: "))
steps = 0

while n != 1:
    if n % 2 == 0:
        n = n / 2
    else:
        n = (3 * n) + 1
    print(str(n) + " is even, so I divide by 2: " + str(n / 2) if n % 2 == 0 else str(n) + " is odd, so I calculate 3n + 1: " + str(3 * n + 1))
    steps += 1

print("The hailstone sequence took " + str(steps) + " steps to reach 1.")
