# Q2.Write a python program, which will implement the following menu driven operations. Different Arithmetic Ops :- i)addition, ii)substraction, iii)multiplication, iv)division, v)mod vi)expo vii)exit(). #HW
# arithmetic_ops.py

def add(a,b):
    print("Addition ({}+{})={}".format(a,b,a+b))

def sub(a,b):
    print("Substraction({}-{})={}".format(a,b,a-b))

def mul(a,b):
    print("Multiplication ({}x{})={}".format(a,b,a*b))

def div(a,b):
    print("Division ({}/{})={}".format(a,b,a/b))

def mod(a,b):
    print("Mod({},{})={}".format(a,b,a%b))

def expo(a,b):
    print("Exponentiation({}^{})={}".format(a,b,a**b))

def call():
    while True:
        print("="*40)
        print("\tArithmetic Operations")
        print('='*40)
        print("\t1.Addition\n\t2.Substraction\n\t3.Multiplication\n\t4.Division\n\t5.Modulus\n\t6.Exponentiation\n\t7.Exit")
        ch=int(input("Enter Your Choice : "))
        if ch in [1,2,3,4,5,6]:
            a = float(input("Enter Value of a : "))
            b = float(input("Enter Value of b : "))
            print("-"*40)
            match ch:
                case 1:add(a,b)
                case 2:sub(a,b)
                case 3:mul(a,b)
                case 4:div(a,b)
                case 5:mod(a,b)
                case 6:expo(a,b)
            print("-"*40)
        elif ch==7:
            print("successfully Exited!!!")
            exit()
        else:
            print("Invalid Input!!!\nPlease Try again later...")
#main Program
call()