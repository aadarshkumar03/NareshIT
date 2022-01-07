'''Q13.Write a python program which will accept the numerical integer value and display it's multiplication table by using for loop. #CW
multable.py'''

n=int(input("Enter a Number : "))
if n<=0:
    print("Please Enter a valid Number.")
else:
    for i in range(1,11):
        print("{} x {} = {}".format(n,i,n*i))
print("Program Execution Comleted!!!")
