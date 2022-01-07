'''Q20.Write a python program which will accept numerical integer value and decide whether it is prime or not. #CW
primeNum1.py'''

n=int(input("Enter a Number : "))
for i in range(1,n+1):
    if (i<=1):
        print("{} is Invalid Input".format(i))
    else:
        res=True
        for j in range(2,i):
            if (i%j==0):
                res=False
                break
        if res:
            print("{} is Prime".format(i))
        else:
            print("{} is Not prime".format(i))
