#Mars Exploration | HackerRank

s = 'SOSSPSSQSSOR'

def marsExploration(s):
	n = len(s)
	msgs = int(n/3)
	counter = 0
	for m in range(0,n,3):
		test = s[m:m+3]
		for c in range(len(test)):
			sos = 'SOS'
			if test[c] != sos[c]:
				counter += 1
	return counter

print(marsExploration(s))