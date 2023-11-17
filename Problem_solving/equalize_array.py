#Equalize the Array | HackerRank

arr = [ 6,6,2,1,6 ]

from collections import Counter

def equalizeArray(arr):
	c = Counter(arr)
	m = max(c)
	#print(m)
	max_c = (max(c.values()))
	others = [i for i in arr if i != m]
	#print('others',others)


	return len(others)

print(equalizeArray(arr))


def equalizeArray(arr):
    
    a = []
    set_arr = set(arr)
    for i in set_arr:
        a.append(arr.count(i))
    
    a.remove(max(a))
    return sum(a)