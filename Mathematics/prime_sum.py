n = 5000
primes = {2,3,5,7,11,13,17,19,23,29,31,37}
factors = []
for i in primes:
	if n % i == 0:
		factors.append(i)
		
print(factors)
for i in factors:
	for i in factors:
		print(i)p
	