**Type Casting Techniques in Python:**
- The purpose of Type Casting Techniques in python is that "To Convert one type value into another type of value".
- The process of converting one type of value into another type of value is called "Type Casting".
- Fundamentally we have 5 types of Type Casting Techniques, They are:
    1. int()
    2. float()
    3. bool()
    4. complex()
    5. str()

**1. int():**
- int() is used for converting one type of possible value into int type value.
- **Examples:**
- float value into int value --->Possible.
- bool value into int value ---->Possible.
- complex value into int value ---->Not Possible.
- complex.real and complex.imag into int value ---->Possible
- 'int string' into int value ---->Possible.
- 'float / complex / bool / pure string' into int value ---->Not Possible.

**2. float():**
- float() is for converting possible type of one value into float type value.
- **Examples:**
- int type into float type ---->Possible.
- bool type into float type ---->Possible.
- Complex type into float type ---->Not Possible.
- complex.real and complex.imag into float type ---->Possible.
- 'int string' and 'float string' into float value ---->Possible.
- 'bool / complex / pure string' into float value ---->Not Possible.

**3. bool():**
- bool() is used for conveting possibel type of one value into bool type value.
- ALL NON ZERO VALUES ARE TRUE.
- ALL ZERO VALUES ARE FALSE.
- **Examples:**
- int / float / complex / string ---->Possible.

**4. complex():**
- complex() is used for converting possible type of one value into complex type value.
- **Examples:**
- int type into complex type ---->Possible.
- float type into complex type ---->Possible.
- bool type into complex type ---->Possible.
- 'int / float / bool / complex string' into complex type ---->Possible.
- 'pure string' into complex type ---->Not Possible.

**5. str():**
- str() is used for converting all types of values into str type value.
