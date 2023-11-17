#Bill Division | HackerRank

n,k = 4, 1
bill = [3, 10, 2, 9]
b = 12

def bonAppetit(bill,k,n):
    result = None
    if (sum(bill)/2)-bill[k] == b:
        print('Bon Appetit')
    elif (sum(bill)-bill[k])/2 != b:
        print(int(b-((sum(bill)-bill[k])/2)))
    else:
        print('Bon Appetit')

print(bonAppetit(bill,k,n))