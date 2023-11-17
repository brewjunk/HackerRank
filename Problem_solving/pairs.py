#Pairs | HackerRank

import itertools

k = 1
arr = [1,2,3,4]



def pairs(k,arr):
    p = 0
    out = []
    for i in arr:
        arr.remove(i)
        for j in arr:
            if (i,j) in out or (j,i) in out:
                continue
            else:
                if abs(j-i) == k:
                    out.append((i,j))
    return len(out)

print(pairs(k,arr))

