#Save the Prisoner | HackerRank
n = 559033664
m = 822024089
s = 131746755

def saveThePrisoner(n,m,s):
	seats = []
	for i in range(s,n+1):
		seats.append(i)
	temp_seats = []
	for i in range(1,n+1):
		temp_seats.append(i)
	if m > len(seats):
		count = (int(m/len(seats))+1)
		for i in range(count):
			seats.extend(temp_seats)
		return seats[m-1]
	else:
		return seats[m-1]

print(saveThePrisoner(n,m,s))

#    return(((m+(s-1))%n) if((m+(s-1))%n)!=0 else n)
