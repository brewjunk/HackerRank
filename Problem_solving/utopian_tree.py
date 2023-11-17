#Utopian Tree | HackerRank

t = 3
n = [0,1,4]

def utopianTree(n):
	if n == 0:
		return 1
	elif n == 1:
		return 2
	else:
		height = 1
		cycles = n/2
		while cycles > 0:
			height *= 2
			height += 1
			cycles -= 1
		if n % 2 == 0:
			return height
		else:
			return height-1

for i in n:
	print(utopianTree(i))



