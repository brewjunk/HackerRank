#Linear Algebra - 100th power | HackerRank
import math
A = [[1,math.pow(100,1/100),1,0,1]]


for i in A:
    for q in i:
        print(math.floor(q**100)) #Change the sign and dataset(s) :)

# 1
# 100
# 1
# 0
# 1