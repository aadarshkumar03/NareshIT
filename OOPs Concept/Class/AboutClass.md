## Class:
- Class is one of the distinct featurs of OOPs.
- The purpose of Class is that "To develop Programmer-Defined data type and to develop any Real-Time Application".
- To develop programmer defined data type with classes concept, we use a keyword _"class"_.
- Programatically every class name treated as programmer defined data type.
- In OOPs, Every python program must starts with class concept.

## Def. of class:
- A class is a collection of Data Members and Methods.
- When we define a class, we never get any memory space for Data Members and Methods of a class but whose mempry space is created when we create an object w.r.t. class Name.
- All the values are stored in the form of objects and to create an object we need class definition.

## Syntax for defining a class:
<pre>
class <className>:
    class level Data Members
    def InstanceMethodName(self, list of formal params if any):
        ------Block of Statements--------
        ------Specific Operations--------
        ----Specify Instance Data Members----
        
    @classmethod
    def ClassLevelMethodName(cls, list of formal params if any):
        ------Block of Statements---------
        ------Common Operations------------
        
    @staticmethod
    def StaticMethodName(list of formal params if any):
        --------Block of Statements---------
        -------Utility / Unniversal Operations-----</pre>
