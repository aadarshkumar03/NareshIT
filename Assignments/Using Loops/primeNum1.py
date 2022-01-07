'''Q20.Write a python program which will accept numerical integer value and decide whether it is prime or not. #HW
primeNum1.py'''

n=int(input("Enter a Number : "))
if (n<=0):
    print("Invalid Number")
elif (n==1):
    print("{} is neither Prime not Composite".format(n))
elif n>1:
    for i in ragne(2,n//2):
        if (n%i)==0:
            print(n, "is not a PRIME")
            break
        else:
            print(n,"is a PRIME")
