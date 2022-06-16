"""
    Program of find maximum number
"""
def maximum():
    """
       Function of maximum number
    """
    print("Maximum of two numbers")
    print("======================")
   # no1 = 6
   # no2 = 4
    no1 = int(input("Enter No1: "))
    no2 = int(input("Enter No2: "))
    print("no1: ", no1, "   ", "no2:", no2)

    if no1 > no2:
        print("Maximum no(no1): ", no1)
    else:
        print("Maximum no(no2): ", no2)


maximum()
