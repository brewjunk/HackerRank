
from math import sqrt

def primefactors(n):
	primes = []
	while n % 2 == 0:
			n = n/2
			primes.append(2)
	for i in range(3,int(sqrt(n))+1,2):
		while (n % i == 0):
			      n = n/i
			      primes.append(int(i))
	if n > 1:
		primes.append(n)
	return primes

def is_a_smith_number(n):
	factors = primefactors(n)
	factors_str = ''.join(map(str, factors))
	factors_str = factors_str.replace(".", "" )
	print(factors)
	print(factors_str)
	sum_factors = 0
	for i in factors_str:
		sum_factors += int(i)
	sum_digits = 0
	n_str = str(n)
	for i in n_str:
		sum_digits += int(i)
	if sum_digits == sum_factors:
		return 1
	else:
		return 0

print(is_a_smith_number(2050918644))
