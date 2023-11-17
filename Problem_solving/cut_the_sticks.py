#Cut The Sticks | HackerRank

#STDIN           				Function
#-----           				--------
n = 6               			#arr[] size n = 6
arr = [5, 4, 4, 2, 2, 8]     	#arr = [5, 4, 4, 2, 2, 8]

# def cutTheSticks(arr):
# 	result_arr = []
# 	arr = sorted(arr)
# 	s = 0

# 	for i in arr:
# 		print('Before Cutting:', arr)
# 		s = min(arr) #length to cut
# 		print('s',s)
# 		i -= s
# 		if i == 0:
# 			pass
# 		else:
# 			arr.append(n)
# 		del arr[0]
# 		print('After Cutting:', arr)
# 	return result_arr



def cutTheSticks(arr):
    freq = [0]*1001
    result = [len(arr)]
    print(freq)
    print(result)
    for x in arr:
        freq[x] += 1
        print('freq ', freq[0:10])
    for x in freq:
    	print('result ',result)
    	if x > 0:
            result.append(result[-1] - x)
    return result[:-1]

print(cutTheSticks(arr))

def cutTheSticks(arr):
    counters = []
    while any(arr):
        count = 0
        k = arr.copy()
        kk = list(filter(lambda x: x > 0, k))
        mini = min(kk)
        for i in range(len(arr)):
            if arr[i] > 0:
                arr[i] = arr[i]-mini
                count += 1 
        counters.append(count)
    return counters
#Output..
#6
#4
#2
#1