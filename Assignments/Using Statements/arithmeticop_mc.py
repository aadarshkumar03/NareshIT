'''
Q2.Write a python program, which will implement the following menu driven application :
    i)Addition ii)Substraction iii)Multiplication iv)Division v)Modulus vi)Exponentiation vii)Exit.
using match...case statement
arithmeticop_mc.py
'''

a=float(input("Enter First Value : "))
b=float(input("Enter Second Value : "))
choice=int(input("\n 1.Addition \n 2.Substraction \n 3.Multiplication \n 4.Division \n 5.Modulus \n 6.Exponentiation \n 7.Exit \n Select Your Choice : "))
match choice:
    case 1:
        print("Addition({},{})={}".format(a,b,a+b))
    case 2:
        print("Substraction({},{})={}".format(a,b,a-b))
    case 3:
        print("Multiplication({},{})={}".format(a,b,a*b))
    case 4:
        print("Division({},{})={}".format(a,b,a/b))
    case 5:
        print("Modulus({},{})={}".format(a,b,a%b))
    case 6:
        print("Exponentiation({},{})={}".format(a,b,a**b))
    case 7:
        print("\n Exit Done \n Thank You!!!")
        exit()
    case _:
        print("Please Select Valid Choice Number...")
print("Program Execution Completed!!!")
