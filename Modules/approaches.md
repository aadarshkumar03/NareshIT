**Approaches for re-using Modules:**
- We have two apprpaches to re-use the modules. They are : 
  1. By using import Statement
  2. By using from...import Statement

**1. import Statement:**
- Here *import* is a keyword.
- import statements is used for importing or accessing the information about modules (Variables, Function and Classes) of one program into another program and we can access the Variables, Function and Classes by using ModuleName / AliasName.
- ***Syntaxes:***
<pre>
Syntax-1: import ModuleName

Syntax-2: import ModuleName as AliasName
=> Here AliasName is an alternative Name for ModuleName.

Syntax-3: import Modulename-1 as AliasName-1, ModuleName-2 as AliasName-2...ModuleName-N as AliasName-N

Syntax-4: import ModuleName1, ModuleName2...ModuleName-N</pre>
***Note:*** After import the Modules Names with import Statement, we must access the Variables, Functions and Classes w.r.t. ModuleName / AliasName Otherwise we get _NameError_.

***Syntaxes for accessing Variables, Function Name and Class Name:***
<pre>ModuleName.VariableName
ModuleName.FunctionName
ModuleName.ClassName</pre>

**2. By using from...import Statement:**
- Here *from* and *import* are the keywords.
- from...import Statement is also used for importing or accessing the information avout Modules ( Variables, Functions and Classes) of one program into another program and we can access the Variables, Functions and Classes directly without using Module Name.
- ***Syntaxes:***
<pre>
Syntax-1: from ModuleName import VariableName(s)
                                 FunctionName(s)
                                 ClassName(s)

Syntax-2: from ModuleName import VariableName(s) as AliasName
                                 FunctionName(s) as AliasName
                                 ClassName(s) as AliasName
                                 
Syntax-3: from ModuleName import *</pre>

***Note:*** The modules concept provides the code Re-usability across the programs provided the program (Modules) present in same folder but not able to provide code Re-usability across the Folders / Drives / Environments / Networks / Machines.

***Note:*** To get the code Re-usability across the Folders / Drives / Environments / Networks / Machines, we must go for _packages_.
