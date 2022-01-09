# Q.Define an anonymous function for deciding whether the given number is 0 or +ve or -ve. #HW
# posneg.py
decide=lambda a:"ZERO" if (a==0) else "POSITIVE" if a>0 else "NEGATIVE"
# main program
l=[int(val) for val in input("Enter Values Seperated by Comma:\n").split(",")]
for i in l:
    print("{} is {}".format(i,decide(i)))