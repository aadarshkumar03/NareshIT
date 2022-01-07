#Q2.Write a python program, which will calculate simple interest and total amount of pay. #CW
#simpleint.py

p=float(input("Enter Principle Amount:"))
t=float(input("Enter Time:"))
r=float(input("Enter Rate of Interest:"))

#calcuate si
si=(p*t*r)/100

#calculate total amount to pay
totamt=p+si

print("-"*50)
print("\tSimple Intrest results")
print("-"*50)
print("\tPrinciple Amount={}".format(p))
print("\tTime={}".format(t))
print("\tRate of Interest={}".format(r))
print("-"*50)
print("\tSimple Interest on Princple={}".format(si))
print("\tTotal Amount={}".format(totamt))
print("-"*50)
