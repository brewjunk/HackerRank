#Sales by Math | HackerRank

n = 20

ar = [4, 5, 5, 5, 6, 6, 4, 1, 4, 4, 3, 6, 6, 3, 6, 1, 4, 5, 5, 5]

from collections import Counter

def sockMerchant(n, ar):
	count = (Counter([x for x in ar]))
	pairs = 0
	print(count)
	for p,q in count.items():
	 	if q >= 2:
	 		pairs += q//2
	return pairs



print(sockMerchant(n,ar))