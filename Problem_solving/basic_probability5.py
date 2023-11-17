from itertools import combinations
from itertools import permutations
people= ["A","B","C","D","E","F","G","H","I","J"]
#print(list(permutations(people, 10)))
count = 0
for i in (list(permutations(people, 10))):
    print(i)
    
    count += 1

print(count)