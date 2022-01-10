**Anonymous Function (OR) lambda Functions:**
- Anonymous Functions are those which does not contain any name explicitly.
- The purpose of Anonymous Functions is that "To perform Instant Operations". (Instant Operations are those which are used at that point of time only but no longer interested to in Further Programs).
- To develop instant operation by using Anonymous Function, we use a Keyword called _"lambda"_ and hence Anonymous Functions are called as _lambda Functions"_.
- ***Syntax:*** varname = lambda params-list : Statement

**Explanation:**
1. Here 'varname'is an object of _<class, function'>_.
2. lambda is a keyword which is used to develop Anonymous Function.
3. Param-list represents list of Formal Parameters.
4. 'Statement' represents Single Executable Statement.
5. Anonymous Function returns the value Automatically implicitly (No need to write return statement).

<pre>
Q. Define a Function of addition of two Numbers?
# Normal Function:
def sumop(a,b):
    c=a+b
    return c
res =sumop(10,20)
print(res)

# Anonymous Function
sumop = lambda a,b :a+b
res = sumop(10,20)
print(res) #(or)
print(sumop(10,20))</pre>
