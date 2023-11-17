#Between Arrays | HackerRank

from math import gcd
from math import lcm


def getTotalX(a, b):
    result = 0
    
    # Get LCM of all elements of [a]
    lcm_a = a[0]
    for i in a:
        lcm_a = lcm(lcm_a, i)
    
    # Get GCD of all elements of [b]
    gcd_b = b[0]
    for i in b:
        gcd_b = gcd(gcd_b, i)
    
    multiple = 0
    while multiple <= gcd_b:
        multiple += lcm_a
        
        if gcd_b % multiple == 0:
            result += 1
            
    return result