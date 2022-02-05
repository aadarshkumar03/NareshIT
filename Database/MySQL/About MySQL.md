### 1. import mysql.connector:
- If python program want to communicate with MySQL Database, First we must install _mysql-connector_ module by using _pip_ and later we must import in python program.
- *Example:* 
<pre>import mysql.connector
      (OR)
from mysql.connector import *</pre>

### 2. Pythonprogram must get connection from MySQL Database:
- If a python program want a connection of MySQL Database, We must use a pre-defined function _"connect()"_, which is present in _mysql.connector_ module and it returns an object of _<class, mysql.connecotr.connection>_
<pre>import mysql.connector
varname = mysql.connector.connect(host="DNS/IPAddress", user="root", passwd="root")</pre>
- "varname" is an object of <class, mysql.connector.connection>.
- mysql.connector is called Module Name.
- connect() is a pre-defined functionin mysql connector module.
- Here "passwd" of MySQL Database is "root" (Default).
- Here DNS (Domain Naming Service) represents Name of machine where database softwares resides. The default DNS of every machine is "localhost".
- Here IP Address (Internet Protocol Address) represents four parts Numerical address of a machine where database software resides. The default IP Address of every computer is "127.0.0.1" (also known as Loop back Address).
- *Example:*
<pre>import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", passwd="root")
print("Python program got connection from mySQL")</pre>

### 3. Create an object of cursor:
- The purpose of creating an object of cursor is that "To carry the query from python program and brings the result from database software and Handover to Python program.
- To create an object of cursor, we use pre-defined function called _"cursor()"_, which is present in connect object.
- *Syntax:* varname = connobj.cursor()
- Here "varname" is an object of <class, mysql.connector.cursor>.
- Here "connobj" is an object of <class, mysql.connector.connection>.
- *Example:*
<pre>import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", passwd="root")
cur = con.cursor()
print("type of con=", type(con))   #type of con=(class, mysql.connector.connection)
print("type of cur=", type(cur))   #type of cur=(class, mysql.connector.cursor)</pre>

### 4. Design the query, Place the query in Cursor and Execute:
- A query is request / question to the database from python program.
- To execute any tyoe if query, we use a pre-defined function called _execute()_, which is present in cursor object. (<class, mysql.connector.cursor>).
- *Syntax:* curobj.execute('query')

### 5. Process the result which is available in object:
- This process makes us to understand, retrieve the data from cursor object and display it on the console.
- *Example:* handling exception messages dealing with results.
