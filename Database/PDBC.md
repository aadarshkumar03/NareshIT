## Python DataBase Communication (PDBC):
- The main advantage of Python Database communication (PDBC) or Database Software are :
1. Database softwares are secured All types of RDBMS (Oracle, MySQL, DB2...etc) provides username and passwords.
2. The processing the data present in tables of Database is quite easy.
3. Database softwares are allows us to store large amount of data.
4. The architecture of database softwares remains same on all types of OSes.
5. Hence Database softwares are Highly recommended for achieving Data Persistance.

- To do the programming with python to communication with database softwares, we need two things. They are
   1.. Python Program (Req. Python Software)
   2.Tables on Database (Req. Database Software)

- If python program want to communicate with any database softwares, we need a pre-defined module for corresponding database softwares.
- For dealing with Oracle Database software we need a module called _"cx_Oracle"_.
- For dealing wit MySQL Database we need a module called _"mysql-connector"_.
- All types of Database corresponding modules are in disabled form and to enable them we must install explicitly by using a tool called _"pip"_.
- We use a following Syntax for installing any module.
<pre>pip install ModuleName</pre>
 **Examples:**
 <pre>
 1. Install Oracle Database module 
 pip install cx_Oracle
 
 2. Install MySQL Database module
 pip install mysql-connector</pre>
 
 ### Limitations of Python files:
 1. Files of any programming language is un-secured---> Files concept is unable to provide username and passwords.
 2. Processing the data from files is complex.
 3. Files are unable to store large amount of data.
 4. The architecture of files are differing from one OS to another OS.
