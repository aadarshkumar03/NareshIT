## Various form of except blocks:
**Form-1 : Handling Single Excpetion**
<pre>
try:
    try Block of Statements.
except <exception-class-name>:
    except Block of Statemets
    (User-Friendly Error Messages).</pre>

**Form-2 : Multiuple Exception Handling except block**
- This facility says Handling multiple specific exceptions by single except block and reducing the code.</pre>
<pre>
try:
    try Block of Statements
except <exception-class-name-1>, <exception-class-name-2>...<exception-class-name-n>:
    User Friendly Error Messages
    for all exception.</pre>

**Form-3 : Handling Single excpetion with Alias Name**
- Here alias -name is an object of exception-class-name and it stores default Technical Error Message which is caused due to Exception occurance.
<pre>
try:
    try Block of Statements
except exception-class-name as alias-name:
    print(alias-name)
    This will print Default Technical Error message of exception-class-name.</pre>

**Form-4 : Default except block**
- Default except block must always written at last for handling unknown exceptions.
<pre>
try:
    try Block of Statements
except:
    except Block of Statements</pre>
    
**Form-5 : Default except block with Base / SuperClassName**
- Default except block with BaseException (or) Exception must always written at last for handling all types of unknown exceptions.
<pre>
try:
    try Block of Statements
except:
    try Block of Statements</pre>
    
***Note:Industry always recommended to write First all types of specific exceptions with except blocks and at last we write default except block (Otherwise we get Error).***
