#Viral Advertising | HackerRank


n = 3

def viralAdvertising(n):
	cumulative = (5//2)
	x = 2
	y = 0
	for i in range(1,n):
		y = x*3
		cumulative += (y//2)
		x = (y//2)
	return cumulative

print(viralAdvertising(n))