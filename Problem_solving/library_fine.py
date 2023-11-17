#Library Fine | HackerRank
d1,m1,y1 = 2, 7, 1014
d2,m2,y2 = 1, 1, 1015





def libraryFine(d1, m1, y1, d2, m2, y2):

	if d1 <= d2 and m1 <= m2 and y1 <= y2:
		return 0
	if d1 > d2 and m1 == m2 and y1 == y2:
		return 15*(d1-d2)
	if m1 > m2 and y1 == y2:
		return 500 *(m1-m2)
	if y1 > y2:
		return 10000
	else:
		return 0


print(libraryFine(d1, m1, y1, d2, m2, y2))