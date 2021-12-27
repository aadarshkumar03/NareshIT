**Operations:**<br>
**a) Indexing:**<br>
-The process of obtaining a single value from object by passing valid existing Index is called _Indexing_.<br>
_Syntax: obj[Index]_

**b) Slicing:**<br>
-The process of obtaining range of characters from given object is called _Slicing_.<br><br>
_syntax-1:_ obj[BeginIndex:EndIndex]<br>
This syntax gives range of characters from BeginIndex to EndIndex-1 provided by BeginIndex<EndIndex otherwise we never get any output.<br><br>
_syntax-2:_ obj[BeginIndex:]<br>
If we didn't specify EndIndex then PVM takes EndIndex values as len(obj)-1. Hence BeginIndex<len(strobj)-1.<br><br>
_syntax-3:_ obj[:EndIndex]<br>
If we didn't specify BeginIndex then PVM takes BeginIndex value as Initial Index. Hence BeginIndex < EndIndex-1.<br><br>
_syntax-4:_ obj[:]<br>
If we didn't specify BeginIndex and EndIndex then PVM takes BeginIndex as Initial Index and BeginIndex as len(obj)-1.<br><br>
_syntax-5:_ obj[BeginIndex:EndIndex:Step]<br>
_Rule-1:_ Here all BeginIndex, EndIndex and Step can be Positive and Negative.<br>
_Rule-2:_ If the value of Step is Positive then PVM gives range of characters from BeginIndex to EndIndex-1 in forward direction provided BeginIndex < EndIndex. Otherwise we never get any output.<br>
_Rule-3:_ If the value of step is Negative then PVM gives range if characters frin BeginIndex to EndIndex+1 in backward direction provided BeginIndex > EndIndex. Otherwise we never get any output.<br>
_Rule-4:_ In forward direction, If the EndIndex value is 0 then we never et any output.<br>
_Rule-5:_ In backward direction, if the EndIndex value is -1 then we never get any output.<br>
