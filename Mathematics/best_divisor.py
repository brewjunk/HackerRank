#
# from functools import reduce
#
# def factors(n):
#     return set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
#
# if __name__ == '__main__':
#     n = int(input().strip())
#     factors = factors(n)
#     best_divisor = 0
#     best_so_far = 0
#
#     num_sum = 0
#     for num in factors :
#         for x in str(num):
#             num_sum += int(x)
#         if num_sum > best_so_far:
#             best_so_far = num_sum
#             if len(str(num)) <= len(str(best_so_far)):
#                 best_divisor = num
#         num_sum = 0
#     print(best_divisor)
#
#
# ##


def best_divisor(n):
    divs = [i for i in range(1,n+1) if n%i==0]
    return max(divs, key=lambda x: sum(int(i) for i in str(x)))
if __name__ == '__main__':
    n = int(input().strip())
    print(best_divisor(n))
