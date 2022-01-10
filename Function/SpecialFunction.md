**Special Functions in Python Programming:**
- In python Programming, we have 3 types of Special Functions. They are :
    - filter()
    - map()
    - reduce()

**1. filter():**
- The purpose of filter() is that "To filter out some element from list of elements by applying to the Function".
- ***Syntax:*** ObjectName = filter(FunctionName, Iterable_Object)
- ***Explanation:***
  - "ObjectName" is type of <class, 'filter'> and it contains filtered elements and an object of filter can be converted into any iterable_object type.
  - "FunctionName" is either Normal Function or Anonymous Function Name.
  - "Iterabble_Object" can be str, bytes, bytearray, range, list, tuple, set, dict.
  - The execution behaviour of filter() is that "filter() applies every element of iterable_object to the function name, if the function name returns True then that elements will      filtered Otherwise neglected (or not filtered)".

**2. map():**
- The purpose of map() is that "To get new list of elements from old list of elements b applying to the function".
- ***Syntax:*** ObjectName = map(FunctionName, Iterable_Object)
- ***Explanantion:***
  - "ObjectName" is type of <class, 'map'> and it contains new list of elements and an object of map can be converted into any Iterable_Object type.
  - "FunctionName" is either Normal Function or Anonymous Function Name.
  - "Iterable_Object" can be str, bytes, bytearray, range, list, tuple, set, dict.
  - The execution behaviour of map() is thta "map() applies every element of Iterable_Object to the FunctionName and obtains new list of elements based on the logic".

**3. reduce():**
- The purpose of reduce() is that "To obtain single result from list of elements by applying to the Function".
- reduce() present in pre-defined module called "Functools".
- ***Syntax:*** VarName = functools.reduce(FunctionName, Iterable_Object)
- "VarName" is of type int, float, bool, complex and str.
- ***Internal Flow of reduce():***
  - Step-1: reduce() selects first two element of any Iterable_Object and place them in first variable and second variable (say a,b)
  - Step-2 : reduce() applies the first and second variable values to the function and computed and resultant value placed in first variable (say a).
  - Step-3 : reduce() select next succeding element from Iterable_Object and place in into second variable (say b).
  - Step-4 : Repeate (step-2 and step-3) until all elements of Iterabel_Object completed.
  - Step-5 : reduce() automatically return result of First Variable (say a).
