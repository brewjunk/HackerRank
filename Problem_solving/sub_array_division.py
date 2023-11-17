#Sub Array Division | HackerRank

def birthday(s, d, m):
    count = 0
    #print(s)
    for i in range((len(s)+1)-m):
        print(s[i:i+m])
        print('>>>>')
        if sum(s[i:i+m]) == d:
            print('FOUND!')
            print(s[i:i+m])
            count += 1
    return count


s = list(map(int, '3 5 4 1 2 5 3 4 3 2 1 1 2 4 2 3 4 5 3 1 2 5 4 5 4 1 1 5 3 1 4 5 2 3 2 5 2 5 2 2 1 5 3 2 5 1 2 4 3 1 5 1 3 3 5'.split()))
d = 18
m = 6


print(birthday(s,d,m))