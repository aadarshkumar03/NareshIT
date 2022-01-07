'''Q29.Write a python program which will decide the prime numbers b/w 1 to n. #HW
Nthprimes.py'''

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
