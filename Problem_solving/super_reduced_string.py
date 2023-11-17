#Super Reduce String | HackerRank


s= 'aaabccddd'

def superReducedString(s):
    result = ""
    for i in range(len(s)):
        if len(result) == 0 or s[i] != result[-1]:
            result += s[i]
        else:
            result = result[:-1]
            
    return result if len(result) > 0 else "Empty String"

print(superReducedString(s))
