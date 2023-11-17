#Points on a Rectangle | HackerRank

q = 2
n = 3
coordinates = [ [0,0], [0,2], [2, 0], [1, 1] ]

def solve(coordinates):

    d = dict(coordinates)
    print(d)
    y = d.values()
    x = d.keys()

    min_x = min(x)
    max_x = max(x)
    min_y = min(y)
    max_y = max(y)

    ret = "YES"
    for el in coordinates:
        if (el[0] > min_x) & (el[0] < max_x) & (el[1] > min_y) & (el[1] < max_y):
            ret = "NO"
            break
    return ret

x = solve(coordinates)
print(x)

