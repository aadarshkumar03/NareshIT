**V) Dict Data Type:**
- 'dict' is one of the pre-defined class and treated as dict data type.
- The purpose of dict data type is that "To store the data in the form(Key,Value)".
- In (key,Value), The values of key are Unique and Values of Value may or may not unique.
- The elements of dict must organized in the form of curly braces {} and in which we represent {Key:Value}.
- **Syntax: dictobj={key1:val1, key2:val2...key-n:val-n}**
- Here, key1, key2...key-n are values of key and they are unique and they are **_Immutable_** and val1, val2...val-n are values of value and they are may or may not ve Unique and they are **_Mutable_**.
- On the object of dict, we can't apply **_Indexing and Slicing_**.
- An empty dict is one, which does not contain any elements.
  - Syntax:
  - dictobj={}  (OR)
  - dictobj=dict()
- Syntax for adding (Key, Value) to empty dict.
   - dictobj[key1]=value1
   - dictobj[key2]=value2
   - dictobj[key-n]=value-n
- An non-empty dict is one, which contains elements.
- Example:  {key1:val1, key2:val2....key-n:val-n}

**Pre-defined Functions in dict data type:**<br>
**1. clear(): dictobj.clear()**<br>
This function clears / removes all the elements of dict object.

**2. pop(): dictobj.pop(key)**<br>
This is used for removing (Key,Value) from dictobject based on Key, which we passing.<br>
If key does not exist in dict object then we get KeyError.

**3. popitem(): dictobj.popitem()**<br>
This function removes last (Key,Value) of dict oject when it is not empty, Otherwise we get KeyError.

**4. copy(): dictobj1=dictobj2.copy()**<br>
This function copy the content pf the one dict object into another dict object (Shallow copy).

**5. get(): value=dictobj.get(Key)**<br>
This function is used for obtaining value of value by passing value of Key.<br>
If the value of key does not exists then the value of value is "None".

**6. values(): values=dictobj.values()**<br>
This obtains all the values of dict object.<br>
type(values)=dict_values

**7. keys: keys=dictobj.keys()**<br>
This obtains all the keys of dict object.<br>
type(keys)=dict_keys

**8.items(): keysvalues=dictobj.items()**<br>
This obtains all (Key,Value) from dict object.<br>
type(keysvalues)=dict_items

**9. update(): dictobj1.update(dictobj2)**<br>
This function update the (Key,Value) of dictobj1 with (Key,Value) of dictobj2.
