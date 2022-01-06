**Inner or Nested Loops:**
- The process of writing one loop in another loop is called **Inner / Nested Loops**.
- The execution process of inner loops is that "For every value of outer loop inner loop will execute for finite number of times until condition becomes False.

- *Syntax-1:*
<pre>
for var-1 in Iterable_Object-1: #Outer for loop
    ----------------
    for var-2 in Iterable_Object-2:  #Inner for loop
        ---------------
        ---------------
        ---------------
    -------------------
-----------------------</pre>
        
- _Syntax-2:_
<pre>
while (test condition-1):  #Outer while loop
    ------------------
    while (test condition-2):   #Inner while loop
        --------------
        --------------
    --------------
------------------</pre>

- _Syntax-3:_
<pre>
for var in Iteranle_Object:    #Outer for loop
    -----------------
    while (test condition):   #Inner while loop
        ------------
        ------------
    -----------------
------------------</pre>

- _Syntax-4:_
<pre>
while (test condition):   #Outer while loop
    -----------------
    for var in Iterable_Object:   #Inner for loop
        ---------------
        ---------------
    -------------------
-----------------------</pre>
