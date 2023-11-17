#Camel Case | HackerRank

def camelcase(s):
	return (sum(1 for c in s if c.isupper()))+1

print(camelcase('saveChangesInTheEditor'))



