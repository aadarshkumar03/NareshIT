# Q.Write a python program, which will find sum of negative numbers of list of elements. #HW
# negsum.py
from functools import reduce
l=[int(i) for i in input("Enter Numbers Seperated by Comma :\n").split(",")]
negnum=list(filter(lambda a:a<0,l))
negsum=reduce(lambda a,b:a+b,negnum)
print("Origional List :\n{}".format(l))
print("Negative Numbers :\n{}".format(negnum))
print("Sum of Negative Numbers={}".format(negsum))