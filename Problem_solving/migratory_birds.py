#Migratory Birds | HackerRank

from collections import Counter

def migratoryBirds(arr):
    count = (Counter([x for x in arr]))
    most_frequent = (0,0)
    for x,y in sorted(count.items()):
        if most_frequent[1] == 0:
            most_frequent = x,y
        elif most_frequent[1] == y:
            pass
        elif y > most_frequent[1]:
            most_frequent = x,y
    return most_frequent[0]
