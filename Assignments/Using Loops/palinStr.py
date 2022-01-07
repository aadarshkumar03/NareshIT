'''Q12.Write a python program which will accept string and check whether it is palindrome or not. #HW
palinStr.py'''

a=input("Enter String/Word : ")
if a==a[::-1]:
    print("{} is Palindrome".format(a))
else:
    print("{} is not Palindrome".format(a))
print("Program Executed!!!")
