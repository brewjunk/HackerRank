#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a DOUBLE.
# The function accepts 2D_INTEGER_ARRAY coordinates as parameter.
def dist(x1,y1):
    return math.sqrt(x1**2 + y1**2)

def solve(crd):
    # Write your code here
    new=[]
    xi=[p[0] for p in crd if p[1]==0]
    yi=[p[1] for p in crd if p[0]==0]
    new.append(max(xi)-min(xi))
    new.append(max(yi)- min(yi))
    a=max(abs(min(xi)),abs(max(xi)))
    b=max(abs(min(yi)),abs(max(yi)))
    new.append(dist(a,b))
    return max(new)
# def dist(x1,y1):
#     return math.sqrt(x1**2 + y1**2)
# def solve(coordinates):
#     #print(coordinates)
#     x = []
#     y = []
#     for i in coordinates:
#         x.append(i[0])
#         y.append(i[1])
#     #print(x,y)
#     max_x = max(x)
#     #print(max_x)
#     max_y = max(y)
#     #print(max_y)
#     min_x = min(x)
#     #print(min_x)
#     min_y = min(y)
#     print(min_y)
#     if max_x - min_x > max_y - min_y:
#         #print(max_x - min_x)
#         return float(max_x - min_x)
#     else:
#         #print(max_y - min_y)
#         return float(max_y - min_y)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    coordinates = []

    for _ in range(n):
        coordinates.append(list(map(int, input().rstrip().split())))

    result = solve(coordinates)

    fptr.write(str(result) + '\n')

    fptr.close()
