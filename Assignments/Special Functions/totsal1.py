# Q.Write a python program, which will accept old salaries of an employee and obtains the new salary list by giving 10%
# totsal1.py
from functools import reduce
l=[float(i) for i in input("Enter Salaries of Employee seperated by comma :\n").split(",")]
hikesal=list(map(lambda a:a+(a*10/100), l))
totsal=reduce(lambda a,b:a+b, hikesal)
print("Old Salary List :\n{}".format(l))
print("New Salary List :\n{}".format(hikesal))
print("Total Salary Compy paid to their Employees=%0.2f"%totsal)