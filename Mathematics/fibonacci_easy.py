def solve(a, b, n):
    A = a # 9
    B = b # 1..(2)now = 11
    C = A+B
    x = 0
    total = 0
    for i in range(3,n+1):
        print('..F({})..({})'.format(i,total))
        print('{} + {}'.format(total,B))
        total = C + B
        x = A+B
    return total

print(solve(9,1,7))
