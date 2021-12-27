**List:**<br>
- 'list' is one of the pre-defined data type and treated as List Data Type.
- The purpose of list data type is that "To stire multiple values either of same type or different type or both the types with unnique and Duplicate Values".
- To organize the elements if list data type, we must use square brackets []. 
- In otherwords, the elements of list must be enclosed within square brackets [] and seperated by comma.
- We can create empty list with following syntax:<br>
    - listobj=[]<br> (OR)<br>
    listobj=list()<br>
- An object of list maintains Insertion Order(In whichever order we insert the data in list object, in the same order data will be displayed).
- On the object of list, we can perform both **_Indexing and Slicing_** Operations.
- An Object of list belongs to **_Mutable_**.<br>
- we can convert any type valule into list type by using **_list()_**.

**Pre-defined Functions in List:**<br>
**1. append(): listobj.append(value)**<br>
This function is used to adding the eleent at the end of the existing elements of list.

**2. insert(): listobj.insert(index, value)**<br>
This function is used for inserting a value at a specified existing valid Index and it can Positive or Negative.

**3. copy(): obj2=obj1.copy() #Shallow copy**<br>
This function is used for copying the contents of list object into another list object. <br>
This function implements shallow copy.

**4. remove(): listobj.remove(element)**<br>
This function is used for removing First occurence of an element of list object.<br>
If the element is not found in list then we get ValueError.

**5. pop(index): listobj.pop(index)**<br>
This function is used for removing the element of list object based on valid existing Index.<br>
If the Index does not exist then we get IndexError.

**6. pop(): listobj.pop()**<br>
This function is used for removing last element of list object.

**7. clear(): listobj.clear()**<br>
This function is used for removing / clearing all the elements of list object.

**8. index(): listobj.index(element)**<br>
This function is used for finding index of first occurence of specified element.<br>
If the element is not found is list object then we get ValueError.

**9. count(): listobj.count(element)**<br>
This function is used for finding number of occurences of specified element.

**10. reverse(): listobj.reverse()**<br>
This function is used for obtaining reverse order of origional elements of list object.<br>
[ front tp back - Original order and Back to front is called reverse order ]

**11. sort(): listobj(reverse=False/True)**<br>
This function is used for sorting Homogenous elements of list both in ASCending order and DEScending order depends on value of reverse.<br>
Here Default Value of reverse is False and gives in ASCending order.<br>
If reverse is True then gives the elements in DEScending order.

**12. extend(): listobj1.extend(listobj2)**<br>
This function is used for adding the content of one list object to another list object.
