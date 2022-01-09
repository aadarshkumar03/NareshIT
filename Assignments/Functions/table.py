# Q.Write a python program which will generate a multiplication table for a given positive integer value by using function. #CW
#table.py

def table(n):
    if (n<=0):
        print("{} is Invalid input.".format(n))
    else:
        for i in range(1,11):
            print("{}x{}={}".format(n,i,n*i))
#Main program
num=int(input("Enter a number : "))
table(num)