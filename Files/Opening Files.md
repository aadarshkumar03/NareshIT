## Opening the Files:
- In python programming, we have two types of syntaxes to open the files. They are:
    - open()
    - with...open() as

**1.open():**
- ***Syntax:*** 
<pre>varname = open("FileName","FileMode")</pre>
- ***Explanation:***
1. _varname_ is a python valud variable name and treated as pointer to the file and we can call it as _File Pointer_ (always points the file data) and type of varname (File Pointer) is _<class, "\_io.TextIOWrapper">_.
2. _open()_ is pre-defined function used for opening the file.
3. _FileName_ is name of the file.
4. _FileMode_ represents any one of the file opening modes.
5. With this approach, Once we open the file with open() then it is mandatory to close the file manually by using close(). In otherwords open() does not provide auto-closable Operation.

**2.with...open() as:**
- ***Syntax:*** 
<pre>
with open("FileName", "FileMode") as <FilePointer>:
    ------------------------------
    Block of Statements
    ------------------------------
Other statements in Python program.</pre>
- ***Explanation:***
1. _with_ and _as_ are keywords.
2. _open()_ is pre-defined function for opening.
3. _FileName_ is name of the file.
4. _FileMode_ represents any one of the file opening modes.
5. _<FilePointer>_ is a valid variable name points to file data.
6. The advantage of this appraoch is that, it will close the file automatically when PVM comes out of _with...open()...as_ indentation block.
