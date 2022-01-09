# Q.Write a python program, which will calculate total marks of different students who are studying in different classes of different subjects by using functions.#CW
# totmarks.py

def sdetails(sno, sname, sclass, **a):
    print("-"*50)
    print("\tStudent Name : {}".format(sname))
    print("\tStudent Number : {}".format(sno))
    print("\tStudent Class : {}".format(sclass))
    print("-"*40)
    print("\tSubjects\tMarks")
    print("-"*40)
    marks=0
    for k,v in a.items():
        print("\t{}\t\t{}".format(k,v))
        marks=marks+v
    else:
        print("-"*40)
        print("\tTotal Marks  {}".format(marks))
        d=len(a.values())*100
        print("\tPercentage  {}".format((marks/d)*100))
        print("-"*40)

# main program
try:
    sdetails(3,"Aadarsh","XII", Hindi=100,English=78, Math=67, Science=70)
    sdetails(sname="Suresh", sno=48, sclass="Cricket")
except:
    print("\nNo Subjects No Marks")
