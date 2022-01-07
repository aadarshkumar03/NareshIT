# Q4.Write a python program, which will accept an year and decide whether it is leap or not. #HW
# Using Simle if Statement
# leapYear.py

a=int(input("Enter Year : "))
if a%4==0:
    print("{} is Leap Year".format(a))
if a%4!=0:
    print("{} is Not Leap Year".format(a))
print("Program Executed!!")
