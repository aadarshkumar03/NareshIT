# Q.Define an anonymous function whether the given number is even or odd. #CW
# evenodd.py
evenodd=lambda a:"EVEN" if a%2==0 else "ODD"
# main program
l=[int(val) for val in input("Enter Values Seperated By Comma:\n").split(",")]
for i in l:
    print("{} is {}".format(i, evenodd(i)))