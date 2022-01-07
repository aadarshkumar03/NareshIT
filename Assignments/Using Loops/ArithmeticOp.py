'''Q31.Write a python program which will implement the following menu driven application.
    i)Addition ii)Substraction iii)Multiplication iv)Division v)Modulus vi)Exponentiation vii)Exit. #HW
    
ArithmeticOp.py'''

import sys
i=0
while(i<=0):
    print("1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n5.Modulus\n6.Exponentiation\n7.Exit")
    n=int(input("Enter Your Choice : "))
    if n<=0 or n>7:
        print("-"*30)
        print("Please Enter Valid Input!!!")
        print("-"*30)
    elif n==7:
        print("You are Successfully Exited...\nThank you!!!")
        sys.exit()
    else:
        a=float(input("Enter Value of a : "))
        b=float(input("Enter Value of b : "))
        match n:
            case 1:
                print("Addition({}+{})+{}".format(a,b,a+b))
                i+=1
            case 2:
                print("Substraction({}-{})={}".format(a,b,a-b))
                i+=1
            case 3:
                print("Multiplication({}x{})={}".format(a,b,a*b))
                i+=1
            case 4:
                print("Division({}/{})={}".format(a,b,a/b))
                i+=1
            case 5:
                print("Modulus({}%{})={}".format(a,b,a%b))
                i+=1
            case 6:
                print("Exponentiation({}**{})={}".format(a,b,a**b))
                i+=1
