# Q1.Write a python program, which will accept two integer values and decide biggest number. #CW
# Using if...else
# Big_ie.py

a=int(input("Enter First Number : "))
b=int(input("Enter Second Number : "))
if a==b:
    print("ALL VALUES ARE EQUAL!!")
else:
    if a>b:
        print("Big ({},{}) = {}".format(a,b,a))
    else:
        print("Big ({},{}) = {}".format(a,b,b))
print("Program Executed!!!")
