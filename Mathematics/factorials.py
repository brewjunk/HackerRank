#factorials.py
#Version 1.00 (Changed on 12 Jun 18:23)
#!/usr/bin/env python3
import time
while True:
    print("""
              ||||||||||!!||||||||||||||!!||||||||||||||!!||||||||||||||!!||||
              ||||||||||!!||||||||||||||!!||||||||||||||!!||||||||||||||!!||||
              |||||||||||!!|||||||FACTORIALS!||||||||||||!!||||||||||||||!!|||
              |||||||||||!!||||||||||||||!!||||||||||||||!!||||||||||||||!!|||
              In mathematics, the factorial of a non-negative integer (n),
              denoted by (n!), is the product of all positive integers less
              than or equal to (n). The factorial of (n) also equals the
              product of (n) with the next smaller factorial.


    """)
    usr_num = input("              Please enter an integer to find the factorial:")
    start_time = time.time()

    print("              You have entered ", usr_num)
    f_num = int(usr_num)
    count = int(usr_num)
    f_list = []

    for num in range(1,count+1):
        count = count - 1
        f_list.append(num)
    f_list_sorted = sorted(f_list, reverse = True)

    acc = f_num
    it_counter = 1
    for num in f_list_sorted:
        acc = acc * f_list_sorted[it_counter]
        if it_counter == f_num-1:
            continue
        else:
            it_counter += 1
    print("""

              What is factorial {}?

              The value of factorial of {} is {}

    """.format(f_num,f_num,acc))
    x = "x".join(str(item) for item in f_list_sorted)
    print("              The expression for {}! = ".format(f_num),x)
    print("""



    """)
    calc_secs = time.time() - start_time

    print ("          Total calculation time : ", ("%.3f" % calc_secs))
    print("""




    """)
    check = input("""              Would you like to try another set?:
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
    else:
        continue
