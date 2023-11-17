n = int(input().strip())
divisors = {1}
int_sum = []

def getSum(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum

for i in range(2,n):
    sum = 0
if n % i == 0:
    sum = getSum(i)
    if sum > int_sum:
        int_sum.append(sum)
        divisors.add(i)

print(n)
print(int_sum)
