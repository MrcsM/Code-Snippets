# this was for a stats assignment where I had to use SPSS to simulate experiments with a 30% chance of interview and numerous n values
# i couldnt work with spss at the time so i coded this
# i was told use SPSS or i got a 0 so i call this: "the useless garbage machine"
# it works though, it's neat but a complete waste of time on my end

import random

n = 0
chance = 30
relative_freqs = []

print("Starting simulation for experiment of: \n - 30% chance of interview \n - n values: 10, 100, 5000 and 10000.")

ns = [10, 100, 5000, 10000] #put n's in here haha
amt = 0

for i in range(0, 4):
    for num in range(0, ns[i]):
        if (random.randint(0, 100) <= chance):
            amt += 1

    print("End of simulation for n = " + str(ns[i]) + ". Calculating relative frequency.")
    relative_freqs.append(amt / ns[i])

print("############################")
print("### Relative Frequencies ###")
print("############################")
for i in range(0, 4):
    print(" " + str(ns[i]) + " - " + str(relative_freqs[i]))
print("############################")
