'''Q5.Write a python program which will print factors of a given number #HW
factor.py'''

n=int(input("Enter a Number : "))
if n<=0:
    print("Invalid Number")
else:
    i=1
    while i<n:
        if n%i==0:
            print(i)
        i+=1
