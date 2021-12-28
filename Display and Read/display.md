**Syntaxes for Displaying the result:**

**Syntax-1: print()**
- Display Only Value.
- print(val2, val2...val-n)
- (OR)
- print(var1, var2...var-n)
- **Examples:**
>a=10<br>
>print(a)<br>
>print(86)

**Syntax-2: print(messages)**
- Display only messages.
- When we display any message (String Data), it must be enclosed within single and double quotes (or) Tripple single / double quotes.
- **Examples:**
>s1="Python"<br>
>s2="lang"<br>
>print(s1+s2)<br>
>print(s1,s2)<br>
>print(s1+" "+s2)<br>
>print("python", "lang")

**Syntax-3: print(messages / values)**
- Display messages cum values (OR) values cum messages.
- print(message / value) 
- print(message / value with format()).
- **Examples:**
>a=100<br>
>print("Val of a =",a) #Normal<br>
>print("Val of a ={}".format(a))

**Syntax-4:**
- Display messages cum values (OR) Values cum messages with Format Specifiers.
- **Examples:**
>a=10<br>
>b=2.32<br>
>c="Python"
>print("Val of a = %d"%a)<br>
>print("Val of b = %f"%b)<br>
>print("%s is Language"%c)
