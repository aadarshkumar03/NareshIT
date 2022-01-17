## Reading the data from the files:
- To read the data from the file, we have 4 pre-defined functions, which are present in the object of FilePointer. They are:
    - read()
    - read(No. of Chars)
    - readline()
    - readlines()

**1.read():**
- This function reads the entire data of the file in the form of str.
- ***Syntax:*** varname = FilePointer.read()
- ***Example:***
<pre>
# FileReadEx.py --- read()
fname = input("Enter File Name to read the content:")
try:
    with open(fname, "r") as fp:
        filedata = fp.read()
        print("File Data\n")
        print(filedata)
except FileNotFoundError:
    print("\n{} does not exists".format(fname))</pre>
    
**2.read(No. of chars):**
- This function is used for reading number of characters from the given file.
- ***Syntax:*** varname = FilePointer.read(No. of chars)
- ***Example:***
<pre># FileReadEx.py --- read(No. of chars)
# tell() ---> Gives index of File Pointer in File Data
# seek(index) ---> This function will reset the File Pointer to the File Data area.

try:
    with open("addr.info", "r") as rp:
    print("Initial Pos of rp=", rp.tell())
    filedata = rp.read(5)
    print("Now Pos of rp=", rp.tell())
    filedata = rp.read(8)
    print("Now Pos of rp=", rp.tell())
    filedata = rp.read()
    print("Now Pos of rp=", rp.tell())
    rp.seek(0)
    print("Initial Pos of rp=",  rp.tell())
except:
    print("Something went WRONG...")</pre>
    
**3.readline():**
- This function reads one line at a time from the given file in the form of _str_
- ***Syntax:*** varname = FilePointer.readline()
- ***Example:***
<pre># FilereadlineEx.py
try: 
    with open("addr1.info", "r") as fp:
        line = fp.readline()
        while line:
            print(line, end="")
            line = fp.readline()
except FileNotFoundError:
    print("File does not Exists")</pre>
    
**4.readlines():**
- This function reads entire content of the file in the form of list.
- ***Syntax:*** listObj = FilePointer.readlines()
- ***Exammples:***
<pre># FilereadlinesEx.py
try:
    with open("addr1.info", "r") as fp:
        filedatalines = fp.readlines()
        for line in filedatalines:
            print(line, end="")
        else:
            print("\nNo. of line=", len(filedatalines))
except FileNotFoundError:
    print("File does not Exists")</pre>
