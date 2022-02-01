from audioop import avg

from numpy import average


a = str(input("please enter your name :"))
if len(a) >= 10:
    print("user length is greater than 10")
else:
    print("user length is smaller than 10")