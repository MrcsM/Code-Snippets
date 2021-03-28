# you enter a number, it checks if the number is odd or even, if odd then it'll calculate 3n + 1 where n is the current value, or will divide if even. 
# at the end it will tell you how many steps it took to get to the number 1

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
