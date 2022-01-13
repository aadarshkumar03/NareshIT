## Development of Programmer-Defined Exceptions:
- These exceptions developed by Python Programmers and available in Python project and they are used always for dealing with common problems.
- Some of the common problems are :
    - Attempting to enter invalid PIN in ATM Application.
    - Attempting to enter invalid User and password.
    - Attempting to enter more amount than existing balance account...etc.
- In general if END user enters valid INPUT then we get valid Output.
- If END users enters invalid INPUT then it is considered as exception and it must create an object w.r.t. appropriate exception class name and it is developed by Python Programmer.

## Steps for Developing Programmer-Defined Exceptions:
1. Choose the programmer-defined class name.
2. The programmer defined class name must inherit the Exception Handling features _BaseException_ (or) _Exception_ for abnormal termination and hence programmer defined class name is called _Programmer Defined Exception Sub-class_.
3. Save the programmer-defined class on some file name with an extension _.py_.
- ***Example:***
<pre>
Develop Programmer defined Exception Class for Invalid PIN
# pin.py  ---> step-3
       step-1     step-2
class PinError(BaseException):pass
      (or)
class PinError(Exception):pass

Develop Programmer-defined exception class name for invalid user and password.
# login.py
class LoginError(BaseException):pass
      (or)
class LoginError(Exception):pass</pre>
