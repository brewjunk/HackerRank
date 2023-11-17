#Matrix Addition | HackerRank

x = [
[1,2],
[2,3]]
y = [
[4,5],
[7,8]]

r = 0
c = 0
for i in x:
    for q in i:
        print(q*y[r][c]) #Change the sign and dataset(s) :)
        c += 1
    c = 0
    r += 1
    