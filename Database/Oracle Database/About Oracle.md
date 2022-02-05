### 1. import cx_Oracle:
- If a python program want to communicate with Oracle Database then we must import cx_Oracle module.
- *Example:*
<pre>import cx_Oracle
    (or)
from cx_Oracle import *</pre>

### 2. Python program must obtain connection from Oracle Database:
- Before doing any any database operations through python program, Python program must get connection from Oracle Database by using _connect()_, which is present in cx_Oracle.
- *Syntax:*
<pre>varname = cx_Oracle.connect("username/password@DNS/serviceID)
DNS : localhost (or) 127.0.0.1</pre>
- Here _'username/password@DNS/serviceID'_ is called _Connection URL_.
<pre>varname = cx_Oracle.connect("Connection URL")</pre>
- ***Here Connection URL represents the Following:***
- Username : It represents username of Oracle Database.
- Password : It represents Username of Oracle Database.
- DNS  : It is the name of the Machine(DNS) or Address of the Machine(IP Address). where database software installed. The default DNS is Localhost and Default IP Address is 127.0.0.1
- ServiceID : It represents on which name, Oracle Database software is installed in the current working machine. To find service ID of Oracle Database we must use following query at SQL prompt.
<pre>SQL>select * from global_name;</pre>
- "Varname" represents object of _<class, cx_Oracle.Connection>_.
- ***Example:***
<pre>#To get the connectiion of Oracle Database from Python program.
import cx_Oracle
con=cx_Oracle.connect("User/password@localhost/orcl")
cur=con.cursor()
print("Python got conncection from Oracle Database")
      (OR)
import cx_Oracle
con=cx_Oracle.connect("User/password@127.0.0.1/orcl")
cur=con.cursor()
print("Python got connection from Oracle Database")</pre>

### 3. Create an object of cursor:
- Here cursor is an object whose purpose is that "To carry the query from python program to Database software and cursor object brings the result from database software to python program".
- To create an object of cursor, we use a pre-defined function called _cursor()_ which is present in connection oject.
- *Syntas:* curobj = conobj.cursor()
- *Examples:* 
<pre>
import cx_Oracle
conobj = cx_Oracle.connect("User/password@localhost/orcl")
curobj = conobj.cursor()
print("Type of curobj=",type(curobj))    # Type of curobj =(class,cx_Oracle.cursor) </pre>

### 4. Design the query, place it into the object of cursor and execute the qyery:
- Query is a request / question to the database sofware.
- To execute the query, we use a pre-defined function called _execute()_, which is present in cursor object.
- *Syntax:* varname = curobj.execute("query")

### 5. Process the result which is available in cursor object:
- This process makes us to understand retrieve data from cursor object and display it on the console.
- *Examaple:* Handling exception messages dealing with results.
