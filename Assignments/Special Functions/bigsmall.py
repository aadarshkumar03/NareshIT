# Q.Write a python program, which will find biggest and smallest of n number of values. #CW
# bigsmall.py
from functools import reduce
l=[int(i) for i in input("Enter Numbers Seperated by Comma :\n").split(",")]
big=reduce(lambda a,b:a if a>b else b,l)
small=reduce(lambda a,b:a if a<b else b,l)
print("List of Elements/Numbers :\n{}".format(l))
print("Big Number from list={}".format(big))
print("Small Number from list={}".format(small))