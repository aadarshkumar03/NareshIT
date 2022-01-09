# Q.Write a python program which will generate fibonacci numbers within n, where n must be the positive integer value by using function. #CW
#fibonacci.py
def fibonacci(n):
    if (n<=0):
        print("{} is invalid input".format(n))
    else:
        i=1
        n1,n2=0,1
        while (i<=n):
            print(n1)
            n3=n1+n2
            n1=n2
            n2=n3
            #increment i value
            i+=1
#Main Program
num=int(input("Enter How many Fibonacci numbers you want : "))
fibonacci(num)