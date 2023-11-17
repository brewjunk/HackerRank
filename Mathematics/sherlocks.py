n = 265107982
divisors = []
divisors2 = []
from math import sqrt

for i in range(1,int(sqrt(n))+1):
	if n% i == 0:
		divisors.append(i)
for i in divisors:
	divisors2.append(n//i)
factors = divisors+divisors2
print(divisors)
print(divisors2)
d_by_2 = 0
for i in factors:
		if i % 2 == 0:
			d_by_2 +=1

print(d_by_2)
