#Linear Algebra - 1000th power | HackerRank
import math
A = [[
    math.pow(2999,1/1000),
    math.pow(9000,1/1000),
    math.pow(1000,1/1000),
    math.pow(3001,1/1000)]]


for i in A:
    for q in i[:2]:
        print(round(q**1000)*-1) #Change the sign and dataset(s) :)
    for q in i[2:]:
        print(round(q**1000))

# -2999
# -9000
# 1000
# 3001