**2. frozenset:**
- 'frozenset' is a pre-defined class and treated as Set Data Type.
- The purpose of frozenset data type is that "To store multiple values either of same type or different type or both the types with unique values".
- To represent the elements of frozenset, we don't have any symbolic Notation but we can convert any other type elements into frozenset by using **_frozenset_()**.
- **_Syntax = frozenset(Collection types)_**
- We can create an empty frozenset by using **_frozenset()_**.
  - frozensetobj = frozenset()  #Empty frozenset
- An object of frozenset does not maintain insertion order because PVM can display the elements of frozenset in any of It's possibilities.
- An object of frozenset never allows us to perform **_Indexing and Slicing_** Operations because frozenset does not maintain Insertion Order.
- An object of frozenset belongs to **_Immutable_** in the case of item assignment and add().

**Pre-defined functions in frozenset:**<br>
**1. isdisjoint(): frozensetobj1.isdisjoint(frozensetobj2)**<br>
This function return True provided frozenset objects are disjoint (Common elements), Otherwise it returns False.

**2. issubset(): frozensetobj1.issubset(frozensetobj2)**<br>
This function return True provided all the elements of frozensetobj1 present in frozensetobj2, Otherwise it returns False.

**3. issuperset(): frozensetobj1.issuperset(frozensetobj2)**<br>
This function returns True provided all the elements of frozensetobj2 present in frozensetobj1, Otherwise it returns False.

**4. copy(): frozensetobj2=frozensetobj1.copy()**<br>
This function is used for copying the content of one frozenset object to another frozenset object (Shallow Copy).

**5. union(): frozensetobj3=frozensetobj1.union(frozensetobj2)**<br>
This function contains all the elements of frozensetobj1 and frozensetobj2 uniquely and place the result elements in frozensetobj3.

**6. intersection(): frozensetobj3=frozensetobj1.intersection(frozensetobj2)**<br>
This function obtains all the common elements from frozensetobj1 and frozensetobj2 and plcase them in frozensetobj3.

**7. difference(): frozensetobj3=frozensetobj1.difference(frozensetobj2)**<br>
- This function removes common elements from both frozensetobj1 and frozensetobj2 and takes remaining elements from  frozensetobj1 and place them in frozensetobj3.
- **frozensetobj3=frozensetobj2.difference(frozensetobj1)**
- This function removes common elements from both frozensetobj1 and frozensetobj2 and takes remaining elements from frozensetobj2 and place them in frozensetobj3.
- 
**8. symmetric_difference(): frozensetobj3=frozensetobj1.symmetric_difference(frozensetobj2)**<br>
This function removes common elements from both frozensetobj1 and frozensetobj2 and collect remaining elements from frozensetobj1 and frozensetobj2 and place them in frozensetobj3.
