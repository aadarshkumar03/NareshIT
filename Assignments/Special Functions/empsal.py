# Q.Write a python program, Which will accept list of employee salaries and give 2.5% hike to every employee and prepare new salary list with anonymous function by using map function. #CW
# empsal.py
l=[int(i) for i in input("Enter Old Salaries seperated by comms :\n").split(",")]
newsal=list(map(lambda n:n+(n*2.5/100),l))
print("OldSalary\t\tNewSalary")
for i,j in zip(l,newsal):
    print("%s\t\t\t%s"%(i,j))