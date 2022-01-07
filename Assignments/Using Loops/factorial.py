'''Q10.Write a python program which will accept positive numerical integer value and find it's factorial. #CW
factorial.py'''

n=int(input("Enter a Number : "))
if n<0:
    print("Invalid Number.")
else:
    i=1
    r=1
    while i<=n:
        r=r*i
        i+=1
    else:
        print("Factorial of {}={}".format(n,r))
print("Program Executed!!!")
