# ..............
# 21 23 25 27 29
#
# 20 22 24 26 28
#
# 11 13 15 17 19
#
# 10 12 14 16 18
#
#  1  3  5  7  9
#
#  0  2  4  6  8
#
#  6 3
#
#  25

 #!/bin/python3

 import math
 import os
 import random
 import re
 import sys

 #
 # Complete the 'strangeGrid' function below.
 #
 # The function is expected to return an INTEGER.
 # The function accepts following parameters:
 #  1. INTEGER r
 #  2. INTEGER c
 #

 def strangeGrid(r, c):
     if r % 2 == 0:
         x = (r*5)-1
         result = x-((5-c)*2)
     else:
         x = (r*5)+3
         result = x-((5-c)*2)
     return int(result)

 if __name__ == '__main__':
     fptr = open(os.environ['OUTPUT_PATH'], 'w')

     first_multiple_input = input().rstrip().split()

     r = int(first_multiple_input[0])

     c = int(first_multiple_input[1])

     result = strangeGrid(r, c)

     fptr.write(str(result) + '\n')

     fptr.close()
