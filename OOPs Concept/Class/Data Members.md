## Types of Data Members in class of Python:
- In python programming, In a class, we can define two types of Data Members. They are:
    - Instance Data Members 
    - Class Level Data Members

### Instance Data Member:
- Instance Data Members are those, whose memory space is created every time when we create an object and hence Instance Data Members are called Object Level Data Members.
- Instance Data members are used for storing specific values.
- Instance Data members must be specified in two ways. They are:
    - Through an Object
    - Through Instance Method
- Instance Data Members must be accessed w.r.t. object name (or) self
<pre>
objectName.InstanceDataMemberName
          (or)
self.InstanceDataMemberName</pre>

### Class Level Data Members:
- Class Level Data Members are those whose memory space created only once irrespective of number of objects created.
- Class Level Data Members are used for storing common values.
- Class Level Data Members can be specified in 3 ways. They are:
    - Inside of Class Definition
    - Before all Objects Creation (main program)
    - Inside of Class Level Method.
- Class Level Data Members must be accessed w.r.t. ClassName (or) ObjectName (or) self (or) cls.
<pre>
ClassName.ClassLevelDataMemberName
          (or)
cls.ClassLevelDataMemberName
          (or)
objectName.ClassLevelDataMemberName
          (or)
self.ClassLevelDataMemberName</pre>
