## Data Persistancy by using Files:
**Def. of File:**
- A file is collection of records 
- A record is collection of inter-related values.
- File names are always resides in secondary memory.
- A file-name is considered as named location in secondary memory.

**Def. of stream:**
- The flow of data between main memory and file of secondary memory is called __Stream__.
- ***What is flow:*** All objects data of main memory becomes _records_ in files of secondary memory and all the _records_ of files of secondary memory becomes _objects_ in main memory.

**Operations on Files:**
- On files, we can perform two types of operations. They are:
  - write operation
  - read operation

**1. write Operation:**
- The purpose of write operation is that "To transfer the object of main memory into file of Secondary Memory".
- ***Steps:***
  - Choose the file name.
  - Open the file name in write mode.
  - Perform cycle of write Operations.

**2. read Operation:**
- The purpose of read operationis that "To trransfer the record(s) from the file of Secondary Memory into object of main memory".
- ***Steps:***
  - Choose the file name.
  - Open the file name in read mode.
  - Perform cycle of read operations until end-of-file.
