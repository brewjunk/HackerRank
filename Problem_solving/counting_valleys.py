#Counting Valleys | HackerRank

steps = 8

path = ['U','D','D','D','U','D','U','U']

def countingValleys(steps, path):
    valley = False
    current = 0
    count = 0
    for s in path:
    	if s == 'U':
    		current += 1
    		if current == 0:
    			valley = False
    	elif s == 'D':
    		current += -1
    		if valley == False and current < 0:
    			valley = True
    			count += 1
    return count

print(countingValleys(steps, path))


