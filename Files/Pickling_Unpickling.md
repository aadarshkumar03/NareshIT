## Object Serialization (or) Pickling:
- Let us assume there exist an objectc which contains multiple values. To save object data of main memory, if we use normal _write()_ and _writelines()_ then they writes the object data value by value and it is the time consuming process.
- To overcome this problem, we must use _Pickling_ (or) _Object Serialization_.
- In otherwords, The advantage of _Pickling_ (or) _Object Serialization_ is that with single write operation _(dump())_ we can write / save entire object data into file of secondary memory.

***Def. of Pickling (or) Object Serialization:***
- The process of saving / writing the entire object content into the file of secondary memory (Hard Disk) by performing single write operation is called _Pickling_ (or) _Object Serialization_.
- Pickling (or) Object Serialization concept participates in write operation.
- To deal with Pickling (or) Object Serialization we must use pickle module.

***Implementation of Pickling (or) Object Serialization:***
1. import pickle module
2. Create an iterable_object with collection of values.
3. Choose the file and open it into write mode as binary file.
4. Use dump() of pickle module for writing / saving the entire object content into file of secondary memory.
5. **Syntax: pickle.dump(Object, FilePointer)**

## Object De-Serialization (or) Unpickling:
- Let assume there exists a record with multiple values. To read the entire record data from file of secondary memory. If we use read(), read(No. of chars), readline() or readlines() then they reads the values of records value by value and it is one of the time consuming process.
- To overcome this problem, we must use _Unpickling_ (or) _Object De-Serialization_.
- In otherwords, The advantage of _Unpickling_ (or) _Object De-Serialization_ is that wit single read operation _(read())_, we can read entire record content from secondary file into object of main memory.

***Def. of Unpickling (or) Object De-Serialization:***
- The process of reading / retrieving the entire record content from the file of secondary memory into object of main memory by performing single read operation is called _Unpickling_ (or) _Object De-Serialization_.
- Unpickling (or) Object De-Serialization concept participates in read operation.
- To deal with Unpickling (or) Object De-Serialization we must use pickle module.

***Implementation of Unpickling (or) Object De-Serialization:***
1. import pickle module.
2. Choose the file name and open it into read mode as binary file.
3. Use load() pickle module for reading entire record content from file of secondary memory into object of main memory.
4. **Syntax: Objname = pickle.load(FilePointer)**
5. Diaplay the Unpickled / De-Serializaed data which is present in objname.
