## Writing the data to the Files:
- To write te data ti the fuke, we have 2 pre-defined Functions in the object of File Pointer. They are:
    - write()
    - writelines()

**1.write():**
- This function writes the data to the file in form of _str_ always.
- ***Syntax:*** FilePointer.write(str_Data)
- ***Example:***
<pre>
# FileWriteEx.py
fname=input("Enter the file name to write the data:")
with open(fname,"a") as fp:
    fp.write("Guido Van Rossum\n")
    fp.write("3-4, Red Sea Side\n")
    fp.write("Python Software Foundation\n")
    fp.write("Nether Lands\n")
    fp.write(str(500013))
print("Data written to the file")</pre>

**2.writelines:():**
- This function writes the iterable_object to the file in the form of _str_ always.
- ***Syntax:*** FilePointer.writelines(iterable_Object)
- ***Example:*** 
<pre>
# FileWritelinesEx.py
d={10:"Python", 20:"Django", 30:"DS"}
fname=input("Enter the File Name:")
with open(fname, "a") as fp:
    fp.writelines(str(d)+"\n")
print("Data written to the file")</pre>
