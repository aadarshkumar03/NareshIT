# Q.Write a Anonymous function for calculating (a+b)^2. #CW
#sqformula.py
formula=lambda a,b:(a+b)**2
# main program
n1,n2=float(input("Enter First Value : ")), float(input("Enter Second Value : "))
print("({}+{})^2={}".format(n1,n2,formula(n1,n2)))