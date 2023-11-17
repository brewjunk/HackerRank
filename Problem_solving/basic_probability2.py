
X = ['r','r','r','r','b','b','b']
Y = ['r','r','r','r','r','b','b','b','b']
Z = ['r','r','r','r','b','b','b','b']

matched = 0
instance = 0

for x in X:
    for y in Y:
        for z in Z:
            if ([x,y,z].count('r')==2) and ([x,y,z].count('b')==1):
                matched += 1
            instance += 1

print(str(matched//12)+"/"+str(instance//12))
print(str(matched)+"/"+str(instance))