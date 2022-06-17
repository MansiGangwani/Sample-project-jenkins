"""
    Program of find maximum number
"""
import sys

n = len(sys.argv)
print('Argument List:', str(sys.argv))


def maximum():
    """
       Function of maximum number
    """
    print("Maximum of two numbers")
    print("======================")
    # no1 = 6
    # no2 = 4
    no1 = sys.argv[1]
    no2 = sys.argv[2]
    print("no1: ", no1, "   ", "no2:", no2)

    if no1 > no2:
        print("Maximum no(no1): ", no1)
    else:
        print("Maximum no(no2): ", no2)


maximum()
