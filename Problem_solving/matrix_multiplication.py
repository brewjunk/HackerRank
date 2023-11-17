#Matrix_multiplacation | HackerRank

x =[
[5,4,9],
[5,6,67],
[5,6,2]]
y = [
[6,9,5],
[9,9,1],
[3,3,11]]

r = 0
c = 0
for i in x:
    for q in i:
        print(q*y[r][c]) #Change the sign and dataset(s) :)
        c += 1
    c = 0
    r += 1

#30
#36
#45
#45
#54
#67
#15
#18
#22