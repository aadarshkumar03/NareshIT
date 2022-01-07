'''Q6.Write a python program which will calculate sum of first n natural numbers. #CW
naturalSum.py'''

n=int(input("Enter a Number : "))
if n<=0:
    print("Invalid Number")
else:
    i=1
    s=0
    while i<=n:
        print(i, end=" ")
        s=s+i
        i+=1
    else:
        print("\nThe sum of First {} Natural Numbers is {}".format(n,s))
print("Program Executed!!!")
