# Halloween Party

k = int(input())


def halloweenParty(k):
    if k % 2 == 0:
        p = k//2
        return p*p
    else:
        x = (k/2)+0.5
        y = k-x
        return int(x*y)
