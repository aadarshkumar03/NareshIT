**Parameters and Arguments:**
- Parameters are those which are used in Function Definition.
- In python programming, we have two types of paramters. They are : 
    1. Formal Parameters 
    2. Local Parameters
- Formal Parameters are those wich are used in Function Heading and they are always used for storing the INPUT values coming from _Function Call(s)_.
- Local Parameters / Variables are those which are used in Function Body and they are used for storing Temporary Results.
- Arguments are those which are used in Function calls and they are available either in the form of Variable Names or Values.
- All values of Arguments of Function calls are passing to Formal Parameters in Function Heading / Function Definition.

**Types of Arguments / Parameters passing Mechanisms:**
- We know that All values of Arguments of Function calls are passing to Formal Parameter in Function Heading /Function Definition.
- Based on passing the Argument values to Formal parameters, we have 5 types of Arguments and Parameters passing Mechanisms. They are :
    1. Positional Arguments / Parameters
    2. Default Arguments / Parameters
    3. Keyword Arguments / Parameters
    4. Variable Length Arguments / Parameters
    5. Keyword Variable Length Arguments / Parameters

**1. Positional Arguments / Parameters :**
- The concept of positional parameters (or) arguments says that _"The Number of Arguments (Actual Parameters) must be equal to the number of Formal Parameters_".
- This Parameter mechanism also recommends order of Parameters for higher accuracy.
- Python Programming Environment follows by default Positional Parameters.
- ***Syntax:***
<pre>
# Function Definition
def FunctionName(Param1, Param2...Param-n):
    ---------------------------------------------
    Block of statements (Function Body / Logic)
    ---------------------------------------------
# Function Call
FunctionName(arg1, arg2...arg-n)

=> Here,the values of arg1, arg2...arg-n are passing to param1, param2...param-n respectively.</pre>

**2. Default Parameters / Arguments:**
- When there is a common value for family of Function Calls then such type of common values must be takes as Default Parameter with common value (But not recommended to pass by using positional Parameters).
- ***Syntax:***
<pre>
# Function Definition
def FunctionName(Param1, Param2...Param-n1=Val1, Param-n2=Val2...Param-nN=Val-n):
    --------------------------------------------
    Block of Statements (Function Body / Logic)
    --------------------------------------------

=> Here Param-n1, Param-n2...Param-nN are called Default Parameters and Param1, Param2... are called Positional Parameters.</pre>
- ***Rule:*** When we use Default Paramters in Function Definitino, They must be used as last Parameter(s). Otherwise we get Error (SyntaxError:non-Default argument follows default Argument).

**3. Keyword Paramters / Arguments:**
- In some of the circumtances, we know the Function Name and Formal Parameters Name and we don't know the order of Formal Paramter Names and to pass the Data / Values accurately. For that we must use the concept of Keyword Paramters (or) Arguments.
- The implementation of Keyword Paramters / Arguments says that all the Formal Paramter Names used as Arguments in Function Call(s) as Keys.
- ***Syntax:***
<pre>
# Function Definition
def FunctionName(Param1, Param2...Param-n):
    -------------------------------------------
    Block Of Statements (Function Body / Logic)
    -------------------------------------------
# Function Call
FunctionName(Param-n=Val-n, Param1=Val1, Param2=Val2)

=> Here, param-n=Val-n, Param1=Val1, Param2=Val2 are called Keyword Arguments.</pre>

**4. Variable Length Parameters / Arguments:**
- When we have family of multiple Functions Calls with Variable Number of Values / arguments then with Normal Python Programming, we must define multiple Function Definitions. This process leads to more development time. To overcome tgis process, we must use the concept of Variable Length Parameters.
- To implement Variable Length Parameters concept, we must define single function Definition and takes a Formal Parameter precede with a symbol called _astric_ (\*Param) and the Formal paramter astrik symbol is called _Variable Length Parameters_ and whose purpose is to Hold/ Store any Number of Values Coming from similar Function Calls and type is <class, 'tuple'>.
- ***Syntax:***
<pre>
def FunctionName(list of Formal Params, *Param):
    --------------------------------------------
    Block of Statements (Function Body / Logic)
    --------------------------------------------
    
=> Here, *Param is called variable Length Parameter and it can Hold any number of Argument Values (or) 
Variable Number of Argument Vallues and *Param type is <class,'tuple'>.
</pre>
- ***Rule1:*** The\* Param must always written as last of Function Heading and it must be only one (but not multiple).
- ***Rule2:*** When we use Variable Length and Default Parameter in Functin Heading, We use Default Parameter as last and before we use Variable Length Parameter and in Function Calls we should not use Default Parameter as Keyword Argument because Variable Number of Values are treated as Positional Argument Value(s).

**5. Keyword Variable:**
- When we have family of multiple function calls with keyboard variable number of values / arguments then with normal python programming, we must define multiuple Function Definition. This process loads to more developement Time. To Overcome this process, we must use the concept of Keyword Variable Length Parameters.
- To implement Keyword Variable Length Parameters concept, we must define single Function Definition and takes a Formal Parameter preceded with a symbol called _Double astrick_ (\**Param) and the Formal Parameter wit hdouble astrick symbol is called _Keyword Variable Length Paramter_ and whose purpose is to hold / store any number of Keyword Variable Length Values coming from similar Function Calls and whose type is _<class, 'dict'>_.
- ***Syntax:***
<pre>
# Function Definition
def FunctionName(list of formal param, **Param):
    ----------------------------------------------
    Block of Statements (Function Body / Logic)
    ----------------------------------------------</pre>
- Here, \**Param is called _Keyword Variable Length Parameter and it can Hold any number of Keyword Variable Number of argument values and \**Param type is _<class, 'dict'>_.
- ***Rule:*** The \**Param must always written at last part of Function Heading and it must be only one (not multiple).
