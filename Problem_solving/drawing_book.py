#Drawing Book | HackerRank

def pageCount(n, p):
    front = p//2
    back = 0
    if n % 2 != 0:
    	back = int((n-p)/2)
    else:
    	back = int(((n-p)+1)/2)

    if front < back:
    	return front
    else:
    	return back

print(pageCount(5,3))

#return min(p // 2, n // 2 - p // 2)




