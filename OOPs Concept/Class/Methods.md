## Types of Methods in class of Python:
- In a class of python, we can defined three types of methods. They are:
    - Instance Method
    - Class Level Method
    - Static Method

### 1. Instance Method:
- Instance Methods are always used for performing _"Specific (or) Object Level Operaions"_.
- Instance Methods always takes First parameter as _"self"_.
- ***Syntax:***
<pre>
def InstanceMethodName(self, list of formal params if any):
    -----------Block of Statements------------
    -------Specify Instance Data Method-------
    --------Specific Operations---------------</pre>
- Instace Methods can be accessed w.r.t. objectName (or) self.
<pre>
objectName.InstanceMethodName()
        (or)
self.InstanceMethodName()</pre>

### 2. Class Level Method:
- Class Level Methods are always used for performing _"Common operations (or) Class Level Operations"_.
- Every Class level Method definition must be preceded with a pre-defined decorator called _"@classmethod"_ and first formal parameter must be _"cls"_.
- ***Syntax:***
<pre>
@classmethod
def ClassLevelMethodName(cls, list of formal params if any):
    -------------Block of Statements----------------
    ---------Specify Class Level Data Members-------
    ------------Common Operations-------------------</pre>
- Class Level Methods can be accessed w.r.t. className (or) cls (or) objectName (or) self.
<pre>
className.ClassLevelMethodName()
        (or)
cls.ClassLevelMethodName()
        (or)
objectName.ClassLevelMethodName()
        (or)
self.ClassLevelMethodName()</pre>

### 3. Static Method:
- Static Methods are always used for performing _"Utility / Universal Operations"_.
- Every Static Method Definition must be preceded with a pre-defined decorator called _"@staticmethod"_
- Static Method definition will not take _"self"_ or _"cls"_ as formal params.
- ***Syntax:***
<pre>
@staticmethod
def StaticMethodName(list of formal params if any):
    --------------Block of Statements---------------
    ----------Utility / Universal Operations----------</pre>
- Static Method can be accessed w.r.t. className (or) cls (or) objectName (or) self.
<pre>
className.StaticMethodName()
        (or)
cls.StaticMethodName()
        (or)
objectName.StaticMethodName()
        (or)
self.StaticMethodName()</pre>
