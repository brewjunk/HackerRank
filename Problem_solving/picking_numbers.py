#Picking Numbers | HackerRank

n = 6
a = [4, 6, 5, 3, 3, 1]

# def pickingNumbers(a):
# 	s = sorted(a)
# 	count = 0
# 	i = 0
# 	while i+1 < len(s):
# 		print(s[i], s[i+1])
# 		if s[i+1] == s[i]+1 or s[i] == s[i+1]:
# 			count += 1
# 		i += 1
# 	return count




from collections import Counter
def pickingNumbers(a):
    # Write your code here
    arr=Counter(a)
    print(arr)
    m=0
    for i in range(100):
        m = max(m,arr[i]+arr[i+1])
    return m

print(pickingNumbers(a))

def pickingNumbers(a):
    max_lenght = 0
    possible_solutions = {i:list() for i in range(0,101)}

    for i in a:
        possible_solutions[i].append(i)
        if len(possible_solutions[i]) > max_lenght: 
            max_lenght = len(possible_solutions[i])
            
        possible_solutions[i+1].append(i)
        if len(possible_solutions[i+1]) > max_lenght: 
            max_lenght = len(possible_solutions[i+1])
    
    return max_lenght