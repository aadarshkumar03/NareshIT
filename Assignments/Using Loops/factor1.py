'''Q15.Write a python program which will print factors of given number by using for loop #HW
factor1.py'''

n=int(input("Enter a Number : "))
if n<=0:
    print("Invalid Number.")
else:
    for i in range(1,n//2+1):
        if n%i==0:
            print(i)
