#Angry Professor | HackerRank

t = 2
n,k = 4,3
a = [-1,-3,4,2]


def angryProfessor(k, a):
	ontime = 0
	late = 0
	for x in a:
		if x <= 0:
			ontime += 1
		else:
			late += 1
	print(ontime)
	print(late)
	if ontime >= k:
		return 'NO'
	else:
		return 'YES'


print(angryProfessor(k,a))


