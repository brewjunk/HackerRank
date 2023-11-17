#Hurdle Race | HackerRank

n,k = 5, 4
height = [1, 6, 3, 5, 2]

def hurdleRace(k, height):
	if max(height) > k:
		return max(height)-k
	else:
		return 0

print(hurdleRace(k, height))