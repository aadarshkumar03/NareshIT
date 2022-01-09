# Q.Write a python program, which will find sum of positive numbers from list of numbers. #HW
# possum.py
from functools import reduce
l=[int(i) for i in input("Enter Numbers seperated by comma :\n").split(",")]
posnum=list(filter(lambda n:n>0, l))
possum=reduce(lambda a,b:a+b, posnum)
print("Origional List :\n{}".format(l))
print("Positive Numbers From List :\n{}".format(posnum))
print("Sum of Positive Numbers List={}".format(possum))