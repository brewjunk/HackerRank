#Pangrams | HackerRank

s = 'The quick brown fox jumps over the lazy dog'
abc = 'abcdefghijklmnopqrstuvwxyz'
def pangrams(s):
	s = s.lower()
	abc_check = ''
	for letter in s:
		if letter.isalpha() and letter not in abc_check:
			abc_check += letter
	final_string = ''
	for letter in sorted(abc_check):
		final_string += letter
	if final_string == abc:
		result = 'pangram'
	else:
		result = 'not pangram'
	return result

print(pangrams(s))