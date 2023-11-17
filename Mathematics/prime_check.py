import math
def is_prime(n):
  for i in range(2,int(math.sqrt(n))+1):
    if (n%i) == 0:
      return False
  return True

print(is_prime(int(input())))


###
# for (int i = 0; i < 5; i++) 
# {
# Console.WriteLine(i);
# }
###
