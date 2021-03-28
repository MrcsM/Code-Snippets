# this was a midterm question i had in comp1405, it was to make a drawing with a nested loop to where you'd have a pattern of like

# ####1
# ###22
# ##333
# #4444
# 55555

# and i couldnt use any string formatting functions or multiplication
# so this is what i got
# got full marks for the question, and it worked like it should've

rows = 6
num = 1
for row in range(1, rows):
    for j in range(rows - 1, 0, -1):
        if j > row:
            print("#", end='')
        else:
            print(num, end='')
    num += 1
    print("")
