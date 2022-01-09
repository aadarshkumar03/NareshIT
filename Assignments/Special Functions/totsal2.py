# Q.If the salary is less than 10,000 give 20% hike and find the total salary of all employees if the salary more than 10,000 then give 15% hike and find the total salary of total employees. #HW
# totsal2.py

from functools import reduce
l=[float(i) for i in input("Enter Salaries seperated by Comma :\n").split(",")]

# Filtered out salaries
below10=list(filter(lambda a:a<10000,l))
above10=list(filter(lambda a:a>=10000,l))

#Hike in their salaries
hike1=list(map(lambda a:a+(a*20/100),below10))
hike2=list(map(lambda a:a+(a*15/100),above10))

#print old and new salary list
print("Old Salary List ALL of Employees :{}".format(l))
print("New Salary List of={}".format(hike1+hike2))

#Total salary sum
hikesum1=reduce(lambda a,b:a+b,hike1)
hikesum2=reduce(lambda a,b:a+b,hike2)

#print old and new total salary
print("-"*100)
print("Old Total Salary Company paid to their Employees={}".format(reduce(lambda a,b:a+b,l)))
print("New Total Salary Company Paid to their Empolyees={}".format(hikesum1+hikesum2))
print("-"*100)