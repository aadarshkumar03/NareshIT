**Number of Approaches to define FUNCTIONS:**
- **Approach-1**
<pre>
INPUT - Taking from Funciton Call(s) ----> Outside
PROCESS - Function Definition ----> Inside
OUTPUT - Function Call(s) ----> Outside

Example:
# Addition.py
# This program computes addition of two values.
def addop(a,b):
    # Process
    c=a+b
    return c
    
# main program
# Taking INPUTS
k=int(input("Enter First Value : "))
v=int(input("Enter Second Value : "))
# Display Result
res=addop(k,v)
print("Sum={}".format(res))</pre>

- **Approach-2**
<pre>
INPUT - Taking from Function Call(s) ----> Inside
PROCESS - Function Definition ----> Inside
OUTPUT - Function Call(s) ----> Inside

Example:
# Addition.py
# This program computes addition of two values.
def addop():
    # Taking INPUT
    a=float(input("Enter First Value : "))
    b=float(input("Enter Second Value : "))
    # Process
    c=a+b
    # Display Result
    print("Val of a = {}".format(a))
    print("Val of b = {}".format(b))
    print("SUM = {}".format(c))
    
# main program
addop()</pre>

- **Approach-3:**
<pre>
INPUT - Taking from Function Call(s) ----> Outside
PROCESS - Function Definition ----> Inside
OUTPUT - Function Call(s) ----> Inside

Example:
# Addition.py
# This program computes addition of two values.
def addop(a,b):
    # Process
    c=a+b
    # Display Result
    print("Sum({}, {})={}".format(a,b,c))
    
# main program
# Taking INPUT
k=float(input("Enter First Value : "))
v=float(input("Enter Second Value : "))
addop(k,v)</pre>

- **Approach-4:**
<pre>
INPUT - Taking from Function Call(s) ----> Inside
PROCESS - Function Definition ----> Inside
OUTPUT - Function Call(s) ----> Outside

Example:
# Addition.py
# This program computes addition of two values.
def addop():
    # Taking INPUTS
    a=float(input("Enter First Value : "))
    b=float(input("Enter Second Value : "))
    # Process
    c=a+b
    return a,b,c
    
# main program
# Display Result
k,v,r = addop()
print("Sum({},{})={}".format(k.v.r))
print("----------OR----------")
res=addop()   # Here res is a variable / object of type <class, 'tuple'>
print("Sum({},{})={}".format(res[0], res[1], res[2]))</pre>
