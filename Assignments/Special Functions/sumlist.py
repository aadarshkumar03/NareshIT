# Q.Write a python program, which will calculate sum of the elements of list by using reduce function. #CW
# sumlist.py
from functools import  reduce
l=[int(i) for i in input("Enter Numbers Seperated by Comma :\n").split(",")]
sum=(reduce(lambda a,b:a+b, l))
print("List Of Elements / Numbers :\n{}".format(l))
print(sum)