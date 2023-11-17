#John and GCD list
import math


def solve(a):
    #input is a list of numbers. List A
    b = []
    x = a[0]
    print('x', x)
    for item in a:
        print('item in a',item)
        b.append((x*item)//math.gcd(x,item))
        x = item
        print('x in loop', x)
    b.append(a[-1])
    print('a[-1]', a[-1])
    print('b',b)
    return b

list_A = [1,2,3]

print(solve(list_A))
