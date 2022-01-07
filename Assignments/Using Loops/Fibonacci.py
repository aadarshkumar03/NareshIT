'''Q32.Write a python program which will generate fibonacci series. #HW
Fibonacci.py'''

n=int(input("Enter a number for Fibonacci Series : "))
i1,i2=0,1
print("Fibonacci Series : ")
while i1<=n:
    print(i1,end=" ")
    i3=i1+i2
    i1=i2
    i2=i3
