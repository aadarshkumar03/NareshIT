'''Q7.Write a python program which will find sum of squares of first n natural numbers. #CW
naturalSqSum.py'''

n=int(input("Enter a Number : "))
if n<=0:
    print("Invalid Number...")
else:
    i=1
    s=0
    while i<=n:
        print(i**2,end=" ")
        s=s+i**2
        i+=1
    else:
        print("\nThe sum of Square of First {} Natural Numbers={}".format(n,s))
print("Program Executed!!!")
