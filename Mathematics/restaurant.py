from math import sqrt

l,b = (344,734)

def findDivisor(n):
	divisors = []
	for i in range(1,n+1):
		if n% i == 0:
			divisors.append(i)
	return divisors

num = l*b
root = sqrt(num)

if int(root + 0.5) ** 2 == num:
	print('Print1:',1)
else:
	for n in findDivisor(num):
		highest_square = []
		if int(sqrt(n) + 0.5) ** 2 == n and n != 1:
			highest_square.append(int(sqrt(n)))
			print(highest_square)
			print('Print2:',num//(highest_square[-1]*highest_square[-1]))
