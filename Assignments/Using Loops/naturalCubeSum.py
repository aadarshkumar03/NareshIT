'''Q8.Write a python program which will calculate sum of cubes of first n natural numbers #CW
naturalCuveSum.py'''

n=int(input("Enter a Number : "))
if n<=0:
    print("Invalid Number")
else:
    i=1
    s=0
    while i<=n:
        print(i**3, end=" ")
        s=s+i**3
        i+=1
    else:
        print("\nThe sum of cubes of First {} Natural Numbers={}".format(n,s))
print("Program Executed!!!")
