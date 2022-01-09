# Q4.Write a python program which will generate prime numbers within n, where n must be positive integer value by using function. #CW
# prime.py

def prime(n):
    if (n<=1):
        print("{} is Invalid Input".format(n))
    else:
        for i in range(2,n+1):
            res=True
            for j in range(2,i):
                if (i%j==0):
                    res=False
                    break
            if res:
                print("{} is Prime".format(i))
#Main Program
num=int(input("Enter a Number : "))
prime(num)