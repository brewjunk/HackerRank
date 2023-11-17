different_sum6 = 0
total_rolls = 0

for p in range(1,6+1):
    for q in range(1,6+1):
        if (p+q) == 6 and (p != q):
            different_sum6 += 1
        total_rolls += 1

print(str((different_sum6//different_sum6))+"/"+str((total_rolls//different_sum6)))