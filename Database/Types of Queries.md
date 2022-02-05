## Types of Queries 
- A query is a request / question to the Database software to perform various operations.
- In any RDBMS softwares (Oracle, MySQL, DB2, etc...), we have three types of queries. They are
1. DDL (Data Definition Language) Queries.
2. DML (Data Manipulation Language) Queries.
3. DRL (Data Retrieval Lannguage) Queries.

### DDL (Data Definition Language) Queries:
- DDL queries are used to Designing the tables (Physical level) such as create a table, alter a table and drop a table.
- We have 3 types of statements in DDL. They are.
1. create
2. alter
3. drop
#### create:
- This query is used for creating a table.
- *Syntax:*
<pre>SQL>create table <table-name> (Colname1 DataType, Colname2 Datatype....Colname-n DataType-n);</pre>
- *Examples:*
<pre>SQL>create table student(stno number(2), name varchar2(10), marks number(5,2));</pre>
#### alter:
- This query is used for altering the table. In Otherwords - This query can alter the table column sizwes and adding new colummn names.
- *Syntax-1:*
<pre>SQL>alter table <table-name> modify (Existing Colname DataType....);</pre>
- *Syntax-2:*
<pre>SQL>alter table <table-name> add (New Colname DataTye...);</pre>
- *Exampmles:*
<pre>
SQL>alter table Student modify (stno number(3), marks number(6,2));
SQL>alter table student add (Colname Varchar2(11));</pre>
#### drop:
- This query is used for dropping / deleting the table permanently.
- *Syntax:*
<pre>SQL>drop table <table-name>;</pre>
- *Example:*
<pre>SQL>drop table temp;</pre>

### DML (Data Manipulation Language) Queries:
- DML queries are used for performing operations on records / data of the table.
- In RDBMS Software, we have 3 types of DML Statements. They are
1. insert
2. delete
3. update
- Once we use  a DML query then we must use _commit()_ for making permanent changes in a table.
- To undo the operation results we use _rollback()_.
- Here _commit()_ and _rollback()_ present in connection object.
#### insert:
- This query is used for inserting a record in a table.
- *Syntax:*
<pre>SQL>insert into <table-name> values(Val1 for col1, val2 for col2....val-n for col-n);</pre>
- *Example:*
<pre>SQL>insert into student values(102,'Rossum', 1.34);</pre>
#### delete:
- This query is used for deleting either all records or specified recoreds from the given table.
- *Syntax:*
<pre>SQL>delete from <table-name>;
        (OR)
SQL>delete from <table-name> where cond list;</pre>
- *Example:*
<pre>SQL>delete from student;
      (OR)
SQL>delete from student where sno=100;</pre>
#### update:
- This query is used for updating either all recoreds or specified record based on some condition.
- *Syntax:*
<pre>SQL>update <table-name> set colname=val1, colname=val2.....colname-n=val-n;
        (OR)
SQL>update <table-name> set colname1=val1, colname2=val2....colname-n=val-n where cond list;</pre>
- *Example:*
<pre>SQL>update student set sal=5.5, dsg='SE';
      (or)
SQL>update employee set sal=4.4, dsg='SE' where enmae='Rossum';</pre>

### DRL (Data Retrieval Language) Queries:
- DRL (Data Retrieval Language) queries are used for retrieving / reading data / records from the table either all the recoreds or specified records based on condition.
- We use _select_ query as DRL query.
- *Syntax:*
<pre>
Syntax-1
SQL>select col1, col2...col-n from TableName;

Syntax-2
SQL>select col1, col2...col-n from TableName where cond list;

Syntax-3
SQL>select * from TableName;

Syntax-4
SQL>select * from TableName where cond list;</pre>

- Once the select query executed by python program, The records are present in an object of cursor. Now we have extract the records from cursor object by using 3 pre-defined functions. They are
1. fetchone()
2. fetchmany()
3. fetchall()
#### 1.fetchone():
- This is used for obtaining one record at a time from cursor object in form of tuple.
- *Syntax:*
<pre>record = curobj.fetchone()</pre>
#### 2.fetchmany():
- *Syntax:*
<pre>record = curobj.fetchmany(No. of records)</pre>
- This function obtains specified number of records from cursor object. (Specified number of records < Total number of records).
- If number of records are more that total number of records then we get all the records of cursor object.
- If number of records are Negative then we never get any records.
- If number of records are Zero then we get all the records of cursor object.
#### 3.fetchall():
- *Stntax:*
<pre>record = cursorObj.fetchall()</pre>
- This function gives all the records of a cursor object.
