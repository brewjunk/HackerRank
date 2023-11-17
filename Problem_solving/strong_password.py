#Strong Password | HackerRank

numbers = list("0123456789")
lower_case = list("abcdefghijklmnopqrstuvwxyz")
upper_case = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
special_characters = list("!@#$%^&*()-+")

#1 length is at least 6.
#2 contains at least one digit.
#3 contains at least one lowercase English character.
#4 contains at least one uppercase English character.
#5 contains at least one special character. The special characters are: !@#$%^&*()-+

n = 4
password = 'Ab1#'

def minimumNumber(n, password):
    count = 0
    if not(re.search(r'[A-Z]+',password)): count += 1
    if not(re.search(r'[a-z]+',password)): count += 1
    if not(re.search(r'[0-9]+',password)): count += 1
    if not(re.search(r'[!@#$%^&*()+\-]+',password)): count += 1
    if n <= 3 or 6-n >= count: count = 6 - n
    return count

print(minimumNumber(n,password))