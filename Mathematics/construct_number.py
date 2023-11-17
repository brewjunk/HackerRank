T= 3

t = (1,3,2)
n = (9,'40 50 90', '1 4')

for i in range(T):
	q =  t[i]
	if q == 1 and n[i] % 3 == 0:
		print('Yes')
	if q > 1 :
		total = 0
		for i in n[i].split():
			total = total + int(i)
		if total % 3 == 0:
			print('Yes')
		else:
			print('No')
			
			
			
		
	

