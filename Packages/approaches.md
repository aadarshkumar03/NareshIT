**Number of approaches to re-use the modules of packages:**
- We have two approaches to re-use the modules of packages. They are
    1. By using _sys.path.append()_
    2. By using _PYTHONPATH_ Environmental Varable.

**1. By using _sys.path.append()_:**
- ***Syntax:*** sys.path.append("Absolute path of package Name")

**2. By using _PYTHONPATH_ Environmental Variables:**
- PYTHONPATH is one of the keyword for os and hence it is called _Environmental Variables_.
- To set PYTHONPATH, do the following steps:
1. Goto start Button
2. Choose Settings
3. Choose System
4. search for "Environmental Variables"
5. choose _new_
6. type ***PYTHONPATH*** for variable Name
7. Place absolute path of package as Variable Value
8. Choose ok.
- Later Execute the Program Freshly.

**General Structure of Package:**
<pre>
FolderName  ---->PackageName
      __init__.py (Empty File)
      ModuleName-1.py
      ModuleName-2.py
      .
      .
      ModuleName-N.py</pre>
