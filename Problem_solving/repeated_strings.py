# #Repeated String | HackerRank



# def repeatedString(s, n):
# 	if len(s) == 1:
# 		s *= n
# 	while len(s) < n:
# 		s = s+s
# 	#print(s)
# 	x = s.count("a", 0, n)
# 	return x


s = 'abcac'
n = 10

def repeatedString(s, n):
    
    str_length = len(s)
    if "a" not in s:
        return 0
    
    if str_length == 1:
        return n
    
    single_count = s.count("a")
    times = n // str_lengthnm 
    temp_string = s[:n % str_length]
    print(temp_string)
    total_count = single_count * times + temp_string.count("a")
    
    return total_count

print(repeatedString(s,n))
