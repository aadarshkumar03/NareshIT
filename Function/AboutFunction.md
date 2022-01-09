**Introduction to Functions**
- The purpose of functin is that "To perform certain operation and provide code re-usability".
- ***Def. of Function:*** Sub-program (or) A part of main program is called "Function".

**Parts of Functions:**
- When we are dealing with function programming we must ensure that there must exists two parts. They are
  1. Function Definition (Function Heading + Function Body)
  2. Function call
- The particular Function definition exists only once.
- For one Function definition, we can have multiple calls.
- For every Function call there must be Function definition otherwise we get NameError.
- Function definition will execute when we call through it's Function call(s).

**Phases in Function:**
- Function Definition takes INPUT.
- Functino Definition PROCESS the INPUT.
- Function Definition gives RESULT / OUTPUT.

**Suntax:** 
___FunctionHeading + FunctionBody = FunctionDefinition___
<pre>
def FunctionName(List of formal parameters if any): #Function Heading
  """doc string"""                                  #documentation string
  statement-1 
  statement-2
  statement-n                                       #Function Body (Logic of Function)
</pre>

**Explanation:**
1. 'def' is a keyword used for defining programmer-defined functions.
2. 'FunctionName' is a valid variable name and treated as function name and all function names are objects and whose type is <class,'function'>.
3. 'List of formal params' are variable(s) list used in function heading and they are used for storing / holding INPUT's coming from Function Call(s).
4. """doc string""" represents commenting on the functionality of the function. In otherwords, """doc string""" describes the functionality of the function.
5. statement-1, statement-2,...statement-n" (Business Logic) represents set of executable statements provides solution for client Requirement.
6. The variables exclusively used in Function Body are called Local Variables and they are used for storing temporary Values / Results.
7. The values of formal parameters and local variables can be accessed within the corresponding Function Definition but not possible to access in the context of other Function Definition.
