most9 = 0
total_rolls = 0

for p in range(1,6+1):
    for q in range(1,6+1):
        if (p+q) <= 9:
            most9 += 1
        total_rolls += 1



print(str((most9//6))+"/"+str((total_rolls//6)))
