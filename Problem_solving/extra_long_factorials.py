#Extra long factorials | HackerRank

def extraLongFactorials(n):
    total = 1
    for i in range(n,0,-1):
    	total *= i

    return total



    
print(extraLongFactorials(25))
print('15511210043330985984000000')
print('15511210043330985984000000')
