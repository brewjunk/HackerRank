from math import sqrt
def primefactors(n):
    primes = []
    while n % 2 == 0:
        n = n/2
        primes.append(2)
    for i in range(3, int(sqrt(n))+1,2):
        while (n % i == 0):
            n = n/i
            primes.append(int(i))
    if n > 1:
        primes.append(int(n))
    return primes
n = int(input())
factors = (primefactors(n))
print('''The Prime factors of {} are :

        {}

        !'''.format(n, factors))
print('''Now Lets find the primitive roots !''')

tests = set(factors)

for i in sorted(tests):
    print(n//i)
for i in range(n-1):
    print(i**)
