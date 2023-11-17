from math import sqrt


def isperfectsquare(number):
    root = sqrt(number)
    if int(root + 0.5) ** 2 == number:
        return True
    else:
        return False

def restaurant(l,b):
    if l > b:
        num = l
    else:
        num = b
    product = l*b
    divisors = []

    for i in range(1,num+1):
        if l % i == 0 and b % i == 0 :
            divisors.append(i)
    if l == b:
        return 1

    return product//(divisors[-1]**2)
#
# def restaurant(l, b):
#     else:
#       lst = []
#       n = l if l > b else b
#       for i in range(1, n+1):
#         if not l%i and not b%i:
#           lst.append(i)
#       m = max(lst)
#       return (l*b)//(m**2)

for i in range(int(input('Number of cases:'))):
    l = int(input("Enter l!"))
    b = int(input("Enter B!"))
    result = restaurant(l, b)
    print(result)
