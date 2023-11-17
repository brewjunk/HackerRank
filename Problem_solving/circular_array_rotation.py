#Circular Array Rotation | HackerRank

def circularArrayRotation(a,k,queries):
	for i in range(k):
		x = a.pop(-1)
		print('x = '  , x)
		a = [x] + a
	result = []
	for i in queries:
		result.append(a[i])
	return result

k = 2
a = [3,4,5]
queries = [1,2]

def circularArrayRotation(a, k, queries):
    # Write your code here
    while k > len(a):
        k = k % len(a)
    a = a[-k:] + a[0:-k]
    results = []
    for q in queries:
        results.append(a[q])
    return results


print(circularArrayRotation(a,k,queries))
