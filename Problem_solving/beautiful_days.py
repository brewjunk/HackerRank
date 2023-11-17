#Beautiful Day at the movies | HackerRank

def beautifulDays(i, j, k):
	count = 0
	for i in range(i,j+1):
		b = int(str(i)[::-1])
		if (i - b) % k == 0:
			count += 1 
		else:
			pass
	return count

i = 20
j = 23
k = 6


print(beautifulDays(i,j,k))

