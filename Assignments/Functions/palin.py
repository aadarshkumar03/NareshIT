# Q5.Write a python program which will accept a numerical integer value and check whether the given number is palindrome or not. #HW
# palin.py

def palin(n):
    if n<0:
        print("{} is Invalid Input".format(n))
    else:
        n=str(n)
        if (n==n[::-1]):
            print("{} is Palindrome".format(n))
        else:
            print("{} is Not palindrome".format(n))

#main program
num=int(input("Enter a Number : "))
palin(num)

#Another way to check palindrome or not
def palin1(n):
    if (n<0):
        print("{} is Invalid Input".format(n))
    else:
        tn=n
        r=0
        while (n>0):
            d=n%10
            r=r*10+d
            n=n//10
        else:
            if (r==tn):
                print("{} is Palindrome".format(tn))
            else:
                print("{} is Not Palindrome".format(tn))

palin1(num)