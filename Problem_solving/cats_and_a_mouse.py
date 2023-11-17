#Cats and a Mouse | HackerRank

cat_a = 2
cat_b = 5
mouse_c = 4

q = 2 # number of queries
x = cat_a
y = cat_b
z = mouse_c
def catAndMouse(x, y, z):
    if abs(z-x) < abs(z-y):
    	return 'Cat A'
    elif abs(z-x) > abs(z-y):
    	return 'Cat B'
    else:
    	return 'Mouse C'

print(catAndMouse(x,y,z))