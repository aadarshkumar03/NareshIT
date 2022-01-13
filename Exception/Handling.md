## Handling the Exceptions:
- Handling the excpetions is nothing but converting Technical Error Messages into User-Friendly Error Messages.
- To handle the exceptions in Python, we have 5 keywords. They are :
    - try
    - except
    - else
    - finally
    - raise

## Syntax for Handling the exceptions in Python:
<pre>
try:
    Block of Statements
    Generating Exceptions.
except <exception-class-name-1>:
    Block of Statements
    Generating user-Friendly Error Messages.
except <exception-class-name-2>:
    Block of Statements
    Generating user-Friendly Error Messages.
except <exception-class-name-N>:
    Block of Statements
    Generating user-Friendly Error Messages.
else:
    Block of Statements recommended 
    to generate results of the program.
finally:
    Block of Statements
    execute compulsarily.</pre>
    
## Explanation:
**1. try block:**
- It is the block, In which we write block of statements generates exceptions. In otherwords, what are all the statements generating exceptions then those statements must written inside of try block and hence try block is called _exception monnitering block_.
- When an exception occurs in try block, PVM comes out of try block and executes appropriate except block and gives user-Friendly Error Messages.
- After executing appropriate except block, PVm never come back to try block for executing rest of the statements.
- Every try block must be immediatly followed by except block otherwise we get _SyntaxError_.
- Every try block must contain atleast one except block and recommended to write multiple except block for generating multiple User-Friendly Error Message.

**2. except block:**
- It is the block, In which we write block of statements generates User-Friendly Error Messages. In otherwords, excpet block supresses the technical error messages and generates User-friendly error messages and hence except block is called _Exception Processing Block_.
- ***Note:*** Handling Exception = try block + except block.
- except block will execute when there is an exception in try block.
- even though we write except blocks, at any point of time, PVM executes only one except block depends on type of exception occurs in try block depends on type of exception occurs in try block.
- The place of writing except block is after writing try block.

**3. else block:**
- It is the block, In which, we write block of statements displays result of the program.
- else blcok will execute when there is no exception occurs in try block.
- else block to be written after except block.
- writing else vlock is optional.

**4. finally block:**
- It is the block, In which we write block of statements will relinquish (Close/release/give-up/clean) the resources(files,databases), which are obtained in try block.
- finally block will execute compulsarily (if we write finally block).
- finally block to be written after else block.

## Some Cases:
- If exception occurs then PVM Executes:
    - A part of try block
    - An appropriate except block
    - A finally block (if we write)
- If exception does not occurs then PVM Executes:
    - Complete try block
    - else block
    - finally block (If we write).
    
## Exception Handling Chart:
<pre>
Base Exception / Exception <------Super class excpetions in python.

  -->ZeroDivisionError     <------This are pre-defined exception Sub-class names.
  -->ValueError
  -->TypeError
  -->NameError
  -->SyntaxError
  -->IndexError
  -->KeyError
  -->AttributeError
  -->IndentationErrror
  -->ModuleNotFoundError
  -->UnBoundLocalError...etc</pre>

**5. raise keyword:**
- raise keyword is used for hitting / raising / generating the exception when certain condition is satisfied.
- PVM uses raise keyword for hitting Pre-defined exception automatically. wehere as Programmer makes the PVM to use raise keyword to hit programmer-defined exceptions. when certain condition is satisfied.
- ***Syntax:***
<pre>
Syntax-1
if (test condition):
    raise exception-class-name
Syntax-2
def FunctionName(list of formal parmas if any):
    if (test condition):
        raise exception-class-name
    -----------------------------
    -----------------------------</pre>
