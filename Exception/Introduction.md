## Introduction to Exception Handling:
- The main purpose of Exception Handling is that "To develop Robust(Strong) Applications"
- In real time to develop any project, we must choose a language and byusing that language, we can develop the program, compile and execute the programs. During this process we get 3 types of error. They are :
    - Compile Time Errors
    - Logic Errors
    - RunTime Errors
 ## 1. Compile Time Errors:
 - These Error occurs during compilation process. (Source code converted into intermediate code).
 - These Errors are occuring due to syntaxes are not followed.
 - These Errors are solved by programmers at Development Time.
 - ***Examples:***
 <pre>a=10
 b=20
 c=a+   #SyntaxError:Invalid syntax</pre>
 
 ## 2. Logical Errors:
 - These Errors are during Runtime / Execution Time.
 - Theses Errors are pccuring due to Wrong representation of logic.
 - These Errors always gives wrong results.
 - These Errors are solved by programmers at Development Time.
 
 ## 3. Run-Time Errors:
 - These Errors are during Runtime / Execution time.
 - These Errors are occuring due to Invalid / Wrong INPUT entered by application Users / END users.
 - These Errors are solved by programmers at Development Time regarding the Errors or mistakes made by end user with forecasting knowledge of programmer.

## Points to be remembered in Exception Handling:
1. When the application user / END user enters Invalid input then we get Run-Time Errors.
``(Invalid INPUTs ----> RunTime Errors)``
2. By default in language, Tuntime Errors always gives Technical Error Messages.
3. ***Def. of Exception***: Every Run time Error is called Exceprion.
``Invalid Input ----> Run time Error ---> Exception``
4. By default Exceptions(Run time Errors) generates Technical Error Messages. Which are understandable by programmers but not by END users. So, industry is highly recommended to convert Technical Error Messages into User-Friendly Error Messages by using Exception Handling.
5. The process of converting Technical Error Messages into user-Fiendly Error Messages is called _"Exception Handling"_.
6. When an Exception occurs in Python Program then 3 things takes place internally.
    - PVM execution abnormally terminated.
    - PVM comes out of Program Flow.
    - By default, PVM generates Technical Error Messages.
7. To do above steps internally, PVM creates an object of an appropriate Exception class, Hence when an Exception occurs then PVm creates an object of appropriate Exception Class.
8. Hence Every exception in python is treated as an object.
