# Q.Write a python program, which will calculate sum and average of variable number of values which are computed by various students who are leaving in Hyderabad. #CW
# sumavag.py

def sumavg(sname,*marks):
    print("Student Name is {}".format(sname))
    s=0
    for i in marks:
        s=s+i
    else:
        print("Sum = {}".format(s))
        print("Avg = {}".format(s/len(marks)))
# main program
sname=input("Enter Your Name : ")
n1=int(input("Enter marks in n1 : "))
n2=int(input("Enter marks in n2 : "))
n3=int(input("Enter marks in n3 : "))
sumavg(sname,n1,n2,n3)