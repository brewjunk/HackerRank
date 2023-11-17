#Non-Divisible Subset | HackerRank

import itertools

s = [1, 7, 2, 4]
k = 3
n = 4 

def nonDivisibleSubset(k, s):
    return s.count('a') * int(n / len(s)) + s[:n % len(s)].count('a')

#     subsets = set(itertools.permutations(s,2))
#     print(len(subsets))
#     for i in sorted(subsets):
#     	print(i[0])


# def repeatedString(s, n):
#     return s.count('a') * int(n / len(s)) + s[:n % len(s)].count('a')


print(nonDivisibleSubset(k, s))


