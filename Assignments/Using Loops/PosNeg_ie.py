# Q2.Write a python program, which will accept Numerical integer value and decide positive, negative or zero by using if....else statement #HW
# Using if...else
# PosNeg_ie.py

a=int(input("Enter a Number : "))
if a==0:
    print("{} is ZERO".format(a))
else:
    if a>0:
        print("{} is Positive Number".format(a))
    else:
        print("{} is a Negative Number".format(a))
print("Program Executed!!!")
