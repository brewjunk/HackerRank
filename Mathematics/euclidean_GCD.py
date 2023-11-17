#euclidean_GCD.py
#Version 1.00
#!/usr/bin/env python3

import time
while True:
    print("""
          |||||||||!!||||||||||||||!!||||||||||||||||!!||||||||||||||!!|||
          |||||||||!!||||||||||||||!!||||||||||||||||!!||||||||||||||!!|||
          |||||||||!!||FIND GCF USING EUCLIDEAN ALGORITHM|||!||||||||!!|||
          |||||||||!!||||||||||||||!!||||||||||||||||!!||||||||||||||!!|||
          The Euclidean Algorithm for finding GCD(A,B) is as follows:
          If A = 0 then GCD(A,B)=B, since the GCD(0,B)=B, and we can stop.
          If B = 0 then GCD(A,B)=A, since the GCD(A,0)=A, and we can stop.
          Write A in quotient remainder form (A = B⋅Q + R)

    """)
    user_number_pair = input("          Please enter a pair of positive integers separated by a , (comma) >> ")
    start_time = time.time()
    if len(user_number_pair) == 0:
        quit()
    else:
        pass
    list_user_numbers = user_number_pair.split(',')
    a = int(list_user_numbers[0])
    b = int(list_user_numbers[1])
    if a > b:
        pass
    elif b > a:
        temp = b
        b = a
        a = temp
    print("""

        """)
    print("""          | Calculating the GCD using Euclidean Algorithm:

                            The two numbers are {} and {}..""".format(a,b))
    print("""

    """)
    def calculate_GCD(a, b):
        while a or b != 0:
            if a > b and a != 0 and b != 0:
                if a // b >=1:
                    mult = a // b
                r = a - b * mult
                c = b * mult + r
                if a == c:
                    print("          | {} = {}({}) + {}".format(a, b, mult, r))
                a = b
                b = r
                if a == 0:
                    print("          | THE GCD = {}".format(b))
                    break
                elif b == 0:
                    print("""

                    """)
                    print("          /////////////////")
                    print("          | THE GCD = {}".format(a))
                    print("          /////////////////")
                    break
        return(a, b, mult, r)

    calc_GCD = calculate_GCD(a, b)
    print("""



    """)
    calc_secs = time.time() - start_time

    print ("          Total calculation time : ", ("%.3f" % calc_secs))
    print("""




    """)

    check = input("""          Would you like to try another set?:
          (Type 1 to try another, Or 0 to quit!)
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
