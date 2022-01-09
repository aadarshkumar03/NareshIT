# Q.Write a python program, which will calculate simple interest by using lambda function. #HW
# simpint.py
simple=lambda p,t,r:(p*t*r)/100
# main program
p =float(input("Enter Principle Amount : "))
t = float(input("Enter Time period in Years : "))
r = float(input("Enter rate of Interest : "))
print("Simple Interest is {} Rs/month.".format(simple(p,t,r)))