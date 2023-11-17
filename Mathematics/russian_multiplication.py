#3
a,b,k,m = 2,0,9,1000
#0 1 5 10
#8 2 10 1000000000
p = a
q = b
r = k
k = m

def russian_mult(p,q,r,k):
	if r == 0:
		return 1
	elif r == 1:
		return (p % k, q% k)
	elif r % 2 == 0:
		return russian_mult(((p*p - q*q) % k), (2*p*q % k), r/2, k)
	else:
		(pr, qr) = russian_mult(p, q, r-1, k)
		return ((p * pr - q * qr) % k, (p * qr + q * pr) % k)
		
print(russian_mult(p,q,r,k))
		
	


