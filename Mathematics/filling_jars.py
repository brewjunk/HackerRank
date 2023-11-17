#!/bin/python3

import math
import os
import random
import re
import sys

def solve(n, operations):
    array = []
    for i in range(n):
        array.append(0)
    for i in range(len(operations)):
        x = operations[0][0]-1
        y = operations[0][1]
        for i in range(x,y):
            array[i] += operations[0][2]
        operations.pop(0)
    print(sum(array))

    return(sum(array))//len(array)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    operations = []

    for _ in range(m):
        operations.append(list(map(int, input().rstrip().split())))

    result = solve(n, operations)

    fptr.write(str(result) + '\n')

    fptr.close()
