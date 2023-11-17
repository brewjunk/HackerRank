
# B1 = ['r','r','r','r','b','b','b','b','b']
# B2 = ['r','r','r','b','b','b','b','b','b','b']


# matched = 0
# instance = 0

# for x in B1:
#     for y in B2:
#         for z in B2:
#             if ([x,y,z].count('r')==1) and ([x,y,z].count('b')==2):
#                 matched += 1
#             instance += 1
        
# print(str(matched)+"/"+str(instance))
# #print(str(matched)+"/"+str(instance))

from fractions import Fraction

bag1 = ['r']*4 + ['b']*5
bag2 = ['r']*3 + ['b']*7

combo = []
visited = 0

for i in bag1:
    for e, j in enumerate(bag2):
        print(e,j)
        for k in bag2[e+1:]:
            temp = [i, j, k]
            if (temp.count('r') == 1) and (temp.count('b') == 2):
                combo.append(temp)
            
            visited += 1
            
print(Fraction(len(combo), visited))