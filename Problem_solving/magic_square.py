#Magic Square | HackerRank

s = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]

c1 = 0
c2 = 0
c3 = 0
r1 = sum(s[0])
r2 = sum(s[1])
r3 = sum(s[2])
d1 = 0
d2 = 0

counter = 0
counter2 = 2
for i in s:
	c1 += i[0]
	c2 += i[1]
	c3 += i[2]
	d1 += i[counter]
	d2 += i[counter2]
	counter += 1
	counter2 -= 1





print(c1,c2,c3)
print(r1,r2,r3)
print(d1,d2)

	# d2 =

