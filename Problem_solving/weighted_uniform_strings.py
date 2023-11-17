#Weighted Uniform Strings | HackerRank

s = 'abccddde'
queries = [6,1,3,12,5,9,10]


def weightedUniformStrings(s, queries):
    alphabet = string.ascii_lowercase
    
    # get weight for contiguous substrings 
    sub = set()
    last = ''
    value = 0 
    for char in s: 
        weight = alphabet.index(char) + 1 
        if char == last:           
            value += weight
            sub.add(value)
        else: 
            sub.add(weight)
            last = char
            value = weight
            
    # check if queries exist in substring 
    output = ['Yes' if query in sub else 'No' for query in queries] 
            
    return output
