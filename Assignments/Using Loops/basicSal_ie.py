# Q3.Write a python program, which will accept basic salary of an employee and calculate the following :
#         if (basicsal>10000) then give
#             da=20% basicsal
#             ta=15% basicsal
#             hra=15% basicsal
#             ma=5% basicsal
#             gpf=2% basicsal
#             lic=2% basicsal
#         Otherwise
#             da=30% basicsal
#             ta=25% basicsal
#             hra=20% basicsal
#             ma=10% basicsal
#             gpf=1% basicsal
#             lic=1% basicsal #CW

# Using if...else
# basicSal_ie.py

ename=input("Enter Employee Name : ")
eno=int(input("Enter Employee Number : "))
basicsal=float(input("Enter Basic Salary : "))
if basicsal<0:
    print("*"*30)
    print("Enter Valid Salary!!!")
    print("*"*30)
else:
    if basicsal>=10000:
        da=basicsal*(20/100)
        ta=basicsal*(15/100)
        hra=basicsal*(15/100)
        ma=basicsal*(5/100)
        gpf=basicsal*(2/100)
        lic=basicsal*(2/100)
    else: #basicsal<10000:
        da=basicsal*(30/100)
        ta=basicsal*(25/100)
        hra=basicsal*(20/100)
        ma=basicsal*(10/100)
        gpf=basicsal*(1/100)
        lic=basicsal*(1/100)
    netsal=(basicsal+da+ta+ma+hra)-(gpf+lic)
    print("*"*50)
    print("Employee Name is {}".format(ename))
    print("Employee Number={}".format(eno))
    print("Employee Basic Salary={}".format(basicsal))
    print("Employee DA={}".format(da))
    print("Employee TA={}".format(ta))
    print("Employee HRA={}".format(hra))
    print("Employee MA={}".format(ma))
    print("Employee GPF={}".format(gpf))
    print("Employee LIC={}".format(lic))
    print("-"*50)
    print("Employee NetSalary={}".format(netsal))
print("-"*50)
print("Thank You!!!")
print("-"*50)
