#Sherlock and Squares | HackerRank
from math import ceil

q = 1
a = 24
b = 49


# def squares(a,b):
# 	return len([i for i in range(a,b+1) if i**0.5 % 1 == 0])


# def squares(a,b):
# 	low = math.ceil(a**0.5)
# 	high = b**0.5
# 	return (high-low)+1

def squares(a,b):
    return int((b**0.5)-ceil(a**0.5))+1

print(squares(a,b))



# import math
# def squares(a, b):
#     lo = math.ceil(a**0.5)
#     hi = (b**0.5)
#     return int(hi)-int(lo) + 1