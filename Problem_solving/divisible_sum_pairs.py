#Divisible Sum | HackerRank

ar = list(map(int,'92 91 27 20 9 43 73 39 24 54 33 64 27 47 32 58 76 78 33 57 5 22 89 78 64 48 41 39 74 33 45 16 16 72 8 42 52 15 64 86 31 73 87 46 30 86 89 67 82 7 91 8 64 32 97 77 31 32 74 40 70 77 56 25 50 8 61 58 1 30 93 66 15 53 64 1 56 69 3 28 26 76 78 38 5 60 43 30 100 58 4 59 78 85 48 89 74 12 54 38'.split()))
n = 100
k = 31



from itertools import combinations


def divisibleSumPairs(n, k, ar):
    count = 0
    print(n,k,ar)
    print(len(ar))
    pairs = list(combinations(ar, 2))
    for p in pairs:
        print(p[0], p[1])
        if sum(p) % k == 0:
            count += 1 
    return count

print(divisibleSumPairs(n,k,ar))

# from itertools import combinations
#     return len([x for x in list(combinations(ar,2)) if sum(x)%k==0])