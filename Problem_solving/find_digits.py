#Find Digits | HackerRank

t = 2
n = [12, 1012]

def findDigits(n):
	divisors = 0
	for i in str(n):
		if int(i) != 0:
			if n % int(i) == 0:
				divisors += 1
	return divisors


print(findDigits(n[1]))