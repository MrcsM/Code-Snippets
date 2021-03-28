# all it literally did was make a list of 200 random numbers and sort them from smallest to biggest
# was made for a stat assignment, except i just put in the values instead of having them randomized

import random

new_list = []

# init random list
num_list = [random.randrange(0, 300) for _ in range(200)]

# while condition will evaluate to False 
# only when num_list is empty

while num_list:  
    # find index of maximum item
    min_index = num_list.index(min(num_list)) 

    # remove item with pop() and append to sorted list
    new_list.append(num_list.pop(min_index))

print(new_list)
