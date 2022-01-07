'''Q11.Write a python program which will accept numerical integer value and check whether the number is palindrome or not. #CW
palinNum.py'''

n=int(input("Enter a Number : "))
if n<0:
    print("Invalid Number.")
else:
    tn=n
    r=0
    while n>0:
        d=n%10
        r=r*10+d
        n=n//10
    else:
        if r==tn:
            print("{} is Palindrome".format(tn))
        else:
            print("{} Not Palindrome".format(tn))
print("Program Executed!!!")
