#LCD.py
#Version 1.00 (Changed on 12 Jun 18:23)
#!/usr/local/bin python3

#Lowest common multiple or two or more numbers.
import time
while True:
    print("""
          |||||||||||!!||||||||||||||!!||||||||||||||!!||||||||||||||!!|||
          |||||||||||!!||||||||||||||!!||||||||||||||!!||||||||||||||!!|||
          |||||||||||!!||FIND LEAST COMMON DENOMINATOR|||||||||||||||!!|||
          |||||||||||!!||||||||||||||!!||||||||||||||!!||||||||||||||!!|||
          The least common denominator is the smallest number of all the
          common multiples of the denominators when 2 or more fractions
          are given.


    """)
    a = input("          Please enter the first nominator :")
    b = input("                           first denominator :")
    c = input("                           second nominator :")
    d = input("                           second denominator :")
    start_time = time.time()

    print("""          You have entered:

                       {} / {}

                       and

                       {} / {}
             """.format(a,b,c,d))

    #Creating two lists of multiples.
    a_list = []
    b_list = []

    for i in range(1,10**3):
        mult_a = int(b) * i
        a_list.append(mult_a)
    #print("A_LIST:")
    #print(a_list)
    for i in range(1,10**3):
        mult_b = int(d) * i
        b_list.append(mult_b)
        if mult_b in a_list:
            LCD = mult_b
            break
        elif mult_b not in a_list:
            LCD = int(b)*int(d)

    print("""

    """)
    #print("B_LIST")
    #print(b_list)

    print("          The LCD of the two denominators is {}".format(LCD))
    print("""          So, The unsimplified answer is :

                       {} / {}

                       and

                       {} / {}
             """.format((((int(a))*(int(LCD/int(b))))),LCD,(int(c))*(int(LCD/int(d))),LCD))
    print("""



    """)
    calc_secs = time.time() - start_time

    print ("          Total calculation time : ", ("%.3f" % calc_secs))
    print("""




    """)
    check = input("""          Would you like to try another pair?:
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
