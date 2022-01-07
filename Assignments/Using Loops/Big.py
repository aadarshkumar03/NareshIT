# Q2.Write a python program, which will accept three values and decide the biggest among them. #CW
# Using Simple if Statement
# Big.py

a=int(input("Enter First Value : "))
b=int(input("Enter Second Value : "))
c=int(input("Enter Third Value : "))
if a>b and a>c:
    print("Big ({},{},{}) is {}".format(a,b,c,a))
if b>a and b>c:
    print("Big ({},{},{}) is {}".format(a,b,c,b))
if c>a and c>b:
    print("Big ({},{},{}) is {}".format(a,b,c,c))
print("Program Executed!!")
