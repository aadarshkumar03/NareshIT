# Q13.Write a python program, which will accept two numerical values and swap them by using Bitwise XOR. #CW
# LogicalSwap.py

a=int(input("Enter First Numerical Value a:"))
b=int(input("Enter Second Numerical Value b:"))

#printing origional value of a and b
print("Origional Value of a {}".format(a))
print("Orogional value of b {}".format(b))

#Swapping Logic
a=a^b
b=a^b
a=a^b
print("Swapped Value of a is {}".format(a))
print("Swapped Value of b is {}".format(b))
