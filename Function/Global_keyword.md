**Global Keyword:**
- When we want to MODIFY THE GLOBAL VARIABLE Values inside of Function Definition then Global Variable Names must be preceded with Global Keyword. Otherwise we get _"UnboundLocalError"_.
- ***Syntax:***
<pre>
var1 = val1
var2 = val2
var-n = val-n
# var1, var2...var-n are called Global Variable Names
def fun():
    -----------------------------
    global var1, var2...var-n
    # MODIFY var1, var2...var-n
    
def fun():
    ------------------------------
    global var1, var2...var-n
    # MODIFY var1, var2...var-n</pre>
