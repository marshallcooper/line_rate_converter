import math


def convertLineRate():
    speed = input("\nWhat is the speed in Mbps?\n")
    lines = input("\nHow many lines does the customer have?\n")
    linerate = int(speed) * 1100 / int(lines) / 64
    print("\n********************")
    print("*                  *")
    print("*  Linerate = " + str(math.ceil(linerate)) + "   *")
    print("*                  *")
    print("********************\n")
