#primality_prime_list.py
#Version 1.00
#!/usr/bin/env python3
from math import floor
import time
while True:
    print("""
              |||||||||||!!||||||||||||||!!||||||||||||||!!||||||||||||||!!|||
              |||||||||||!!||||||||||||||!!||||||||||||||!!||||||||||||||!!|||
              |||||||||||!!|||||||PRIMALITY TEST|!|||||||!!||||||||||||||!!|||
              |||||||||||!!||||||||||||||!!||||||||||||||!!||||||||||||||!!|||
              This program will create a txt file with all the prime numbers,
              up until and including the number of your choice.

    """)

    n = input("              Please enter a number!")

    def prime_check(n_check):
        for num_try in range(2, floor(n_check**0.5)+1):
            if ((n_check % num_try == 0) & (num_try != n_check)):
                return False
    start_time = time.time()

    with open("prime_txts/" + n +'.txt', 'x') as f:
        print("              Testing up to and including", n)
        print("              ---------------------------------")
        n = int(n)
        count = 0
        primes = []
        for num in range(2,n+1):
            if (prime_check(num)) != False:
                print("              ...........{} is a prime...adding to file.".format(num))
                primes.append(num)
                f.write(str(num))
                f.write(', ')
                count += 1
        f.write('\n')
    print("""
              ***************************************************
    """)
    print("              All the primes up until {}".format(n),"are", primes, '<<{} in total>>'.format(count))
    print("""
              ***************************************************
    """)
    print("""



    """)
    calc_secs = time.time() - start_time

    print ("          Total calculation time : ", ("%.3f" % calc_secs))
    print("""




    """)
    check = input("""              Would you like to try another number?: (Type 1 to try another, Or 0 to quit!)
    """)
    print("""

              |||||||||||!!||||||||||||||!!||||||||||||||!!||||||||||||||!!|||
                  """)
    if check == "0":
        print("                    Ok then, Thanks! Good bye!")
        print("""

              |||||||||||!!||||||||||||||!!||||||||||||||!!||||||||||||||!!|||


""")
        break
    elif check == "1":
        continue
