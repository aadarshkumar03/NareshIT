'''Q17.Write a python program which will print all odd numbers from n to 1. #HW
revOddNum.py'''

n=int(input("Enter a Number : "))
if n<=0:
    print("Invalid Number.")
else:
    print("This are Odd Numbers from {} to 1".format(n))
    for i in range(n,0,-1):
        if i%2!=0:
            print(i,end=" ")
print("\nProgram Executed!!!")
