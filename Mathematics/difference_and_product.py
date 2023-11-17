from math import sqrt

def f(d, p):
    if d < 0:
        return 0
    ret = set()
    D1 = d * d + 4 * p
    if D1 >= 0:
        a = round((d - sqrt(D1)) / 2)
        if a * (d - a) == -p:
            ret.add((a, d - a))  
        a = round((d + sqrt(D1)) / 2)
        if a * (d - a) == -p:
            ret.add((a, d - a))
        a = round((-d - sqrt(D1)) / 2)
        if a * (-d - a) == -p:
            ret.add((a, -d - a))
        a = round((-d + sqrt(D1)) / 2)
        if a * (-d - a) == -p:
            ret.add((a, -d - a))
    return len(ret)
            
t = int(input())
for _ in range(t):
    d, p = map(int, input().split())
    print(f(d, p))


T = 3
input_data = [(1,2),(0,4),(-1,1)]



for i in range(len(input_data)):

    print(f(input_data[i][0],input_data[i][1]))
