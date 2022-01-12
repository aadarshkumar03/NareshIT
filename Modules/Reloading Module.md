**Reloading Module in Python:**
- To reload a module in python, we use a Pre-defined Function called *reload()*, which is present in *imp module* and it was deprecated in favour of *importlib module*.
- **Syntax: import.reload(ModuleName) (or) importlib.reload(ModuleName)--->Recommended**

**Purpose / Situation:**
- _reload()_ reloads a previously imported module. if we have edited the module source file by using an external editor and we want to use the changed valules / new version of previously loaded module then we use _reload()_.

