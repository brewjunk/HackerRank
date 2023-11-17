MOD = 10**9+7

def simplestSum(k, a, b):
    return (s_upto(b,k) - s_upto(a-1,k)) % MOD

def s_upto(n,k):
    '''Sum without formulas, simple no-brainer variant'''
    if n == 0: return 0


    # s_j and imax_j stay the same for n in range imax_(j-1) ... imax_j - 1
    s,i = 0,1
    i_seq = []
    while i <= n:
        s += i
        i_seq.append(i)
        i = i*k +1
    return (s*n - sum(i*(i-1) for i in i_seq)) % MOD

print(simplestSum(2,1,5))
