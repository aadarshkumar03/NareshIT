'''Q4.Write a python program which will generate n to 1. #HW
generateNum1.py'''

n=int(input("Enter a Number : "))
if (n<=0):
    print("Invalid Input....")
else:
    i=n
    while i>=1:
        print(i)
        i-=1
print("Program Executed!!!")
