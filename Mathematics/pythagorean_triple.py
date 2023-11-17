def pythagoreanTriple(a):
    if a % 2 != 0:
        c = (((a**2)+1)//2)
        b = c-1
    elif a % 2 == 0:
        b = int(((a**2)//4)-1)
        c = b+2
    return a,b,c

a = 112453065
triple = pythagoreanTriple(a)

print((' '.join(map(str, triple))))
