**global and local Variables and global():**
- When we come across same Global Variable Names and Local Variable Names in same Function Definition then PVM gives preference for Local Variables but not for Global Variables.
- In this context, To extract / retrieve the Global Variables Names along with Local Variables. We must use global() function and it returns an object of <class, 'dict'> and those dict object stores all Global Variable Names as Keys and Global Variable Values as Value of Value.
- ****Syntax:****
<pre>
var1 = val1
var2 = val2
var-n = val-n       # var1, var2...var-n are called global variables.

def FunctionName():
    var1 = val1
    var2 = val2
    var-n = val-n   # var1, var2...var-n are called Local Variables.
    # Extract the global variables
    dictobj = globals()
    globalVal1 = dictobj['var1']    # dictobj.get('var1') (OR) globals()['var1']
    globalVal2 = dictobj['var2']    # dictobj.get('var2') (OR) globals()['var2']
    globalVal-n = dictobj['var-n']  # dictobj.get('var-n') (OR) globals()['var-n']</pre>
