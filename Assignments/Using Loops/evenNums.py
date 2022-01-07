'''Q2.write a python program which will display even numbers within n, where n must be the positive integer value. #HW
evenNums.py
'''

n=int(input("Enter a Number : "))
if n<=0:
    print("Invalid input")
else:
    i=2
    while i<=n:
        print(i)
        i=i+2
