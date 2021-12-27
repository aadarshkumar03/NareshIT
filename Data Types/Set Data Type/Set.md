**1. Set:**<br>
- 'set' is one of the pre-defined class and treated as set data type.
- The purpose of set data type os that "To store multiple values either of same type or different type or both the types with unique values".
- The element of set must be organized within curly braces {} and elements myst be seperated by comma.
- We can create an empty set and we can convert one type elements into set type by usnig **_set()_**.
  - setobj = set() #empty set
- An object of set does not maintain insertion order because PVM can display the elements of set in any of It's possibility among multiple possibilities.
- An object of set never allows us to perform **_Indexing and Slicing_** Operations because set object does not maintain insetion order.
- An object of set belongs to Both **_Mutable_** (In case of add()) and **_Immutable_** (In case of item assignment. Set object does not support item assignment).

**Pre-defined Functions in set:**<br>
**1. add(): setobj.add(element)**<br>
This function is used for adding an element to set object.

**2. clear(): setobj.clear()**<br>
This function is used for removing all the elements of set object.

**3. copy(): setobj.copy #Shallow copy**<br>
This function is used for copying the content of one setobject tp anpther setobject.

**4. discard(): setobj.discard(element)**<br>
This function is used for removing the specified element.<br>
If element does not exists it doesn't give any type of error.

**5. remove(): setobj.remove(element)**<br>
This function is used for removing the specified element.<br>
IF the element does not exists remove() it gives KeyError.

**6. pop(): setobj.pop()**<br>
This function is used for removing an arbitary element from setobject.

**7. isdisjoint(): setobj.isdisjoint(setobj2)**<br>
This function return True provided set objects are disjoint (Common elements), Otherwise it returns False.

**8. issubset(): setobj1.issubset(setobj2)**<br>
This function return True provided all the elements of setobj1 present in setobj2, Otherwise it returns False.

**9. issuperset(): setobj1.superset(setobj2)**<br>
This function returns True provided all the elements of setobj2 present is setobj1, Otherwise it returns False.

**10. union(): setobj3=setobj1.union(setobj2)**<br>
This function obtains all the elements of setobj1 and setobj2 uniquely and place the result elements in setobj3.

**11. intersection(): setobj3=setobj1.intersection(setobj2)**<br>
This function obtains all the common elements from setobj1 and setobj2 and place result elements into setobj3.

**12. difference(): setobj3=setobj1.difference(setobj2)**<br>
This function removes common elements from both setobj1 and setobj2 and takes remaining elements from setobj1 and place them in setobj3.<br>
(OR) **setobj3=setobj2.difference(setobj1)**<br>
This function removes common elements from both setobj1 and setobj2 and takes remaining elements from setobj2 and place them in setobj3.

**13. symmetric_difference(): setobj3=setobj1.symmetric_difference(setobj2)**<br>
This function removes common elements from setobj1 and setobj2 and collect remaining elements from setobj1 and setobj2 and place them in setobj3.

**14. update(): setobj1.update(setobj2)**<br>
This function adds the all values of setobj2 to setobj1.
