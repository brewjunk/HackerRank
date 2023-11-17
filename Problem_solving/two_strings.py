#Two Strings | HackerRank

p = 2
s1 = hello
s2 = world
#s1 = hi
#s2 = world

def twoStrings(s1, s2):
    for i in s1:
        if i in s2:
            return 'YES'
    return 'NO'

print(twoStrings(s1,s2))