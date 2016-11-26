

# Chapter 6

For Loops Over Indices, Parallel Lists and Strings, and Files

### Indices of List

```python
def merge(L):
    merged = []
    for i in range(0, len(L), 3):
        merged.append(L[i] + L[i + 1] + L[i + 2])
    return merged

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]	
print(merge(l))
```

Very useful to make a new list having sum of 3 numbers by grouping
```
1, 2, 3, 4, 5, 6, 7, 8, 9
=======  =======  ========
      6,      15,       24

```

###  Mystery

```python
def mystery(s):
    """ (str) -> bool
    """
    matches = 0
    for i in range(len(s) // 2):
        if s[i] == s[len(s) - 1 - i]: # <--- How many times is this line reached?
            matches = matches + 1

    return matches == (len(s) // 2)

print(mystery('civil'))
```

Trace the function call mystery('civil') using the Python Visualizer. How many times is the line marked above reached?

Answer: 2

Which is the best docstring description for function mystery?

```
1) Return True if and only if s is equal to the reverse of s.
2) Return True if and only if s[:len(s) // 2] is the same as s[len(s) // 2:].
3) Return True if and only if the number of duplicate characters in s is equal to len(s) // 2.
4) Return True if and only if there are exactly len(s) // 2 characters in s that are the same character.
```
Answer: 1)

---
### Shift Right

```python
def shift_right(L):
    ''' (list) -> NoneType

    Shift each item in L one position to the rightand shift the    last item to the first position.

    Precondition: len(L) >= 1
    '''

    last_item = L[-1]

    # MISSING CODE GOES HERE

    L[0] = last_item
	

l = [1,2,3,5,6]	 
print(shift_right(l))
```
Hint: the correct answer works from the end to the beginning of L.

```python
    # 1) Not working properly because of overwrting
    for i in range(0,len(L)-1):
       print(str(L[i]) + "," + str(L[i+1]))	
        L[i+1] = L[i]		
    
    # 2) Good..
    for i in range(1, len(L)):
        L[len(L) - i] = L[len(L) - i - 1]
	
```

---
### Indexing 

Using numbers and indexing with non-negative indices, write an expression that evaluates to 7. Do not use addition, subtraction, or parentheses ( ) (brackets ([] are required).
```python
numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(numbers[2][0])
```

Using treats and indexing with only negative indices, write an expression that evaluates to 'pie'. Do not use addition, subtraction, or parentheses ( ) (brackets[ ] are required).

```python
treats = [['apple', 'pie'], ['vanilla', 'ice-cream'], ['chocolate', 'cake']]

print(treats[-3][-1])

```
---

# String

### for loop

Part of the body of the following function is missing. Select the missing code fragment.

```python
def common_chars(s1, s2):
    '''(str, str) -> str

    Return a new string containing all characters from s1 that     appear at leastonce in s2. The characters in the result        will appear in the same order asthey appear in s1.

    >>> common_chars('abc', 'ad')
    'a'
    >>> common_chars('a', 'a')
    'a' 
    >>> common_chars('abb', 'ab')
    'abb' 
    >>> common_chars('abracadabra', 'ra')
    'araaara'
    '''


    res = ''

    # BODY MISSING
    
    return res
    
    
    # 1)
    if ch in s2:
        for ch in s1:
            res = res + ch
		# 2)
    for ch in s2:
        if ch in s1:
            res = res + ch
            
    # 3)
    for ch in s1:
        if ch in s2:
            res = res + ch

    # 4)
    for ch in s1:
        if ch in s2:
            res = ch + res
```
Answer: 3) and  4)

---

### index

Variables s1 and s2 refer to strs. The expression s1.find(s2) returns the index of the first occurrence of s2 in s1. 
The expression s1.find(s2, 5) returns the index of the first occurrence of s2 in s1, starting at index 5 within s1. 
(See help(str.find) for more info)

Write an expression that produces the index of the second occurrence of s2 in s1. 
If s2 does not occur twice in s1, the expression should produce -1. 
Unlike str.count, you should allow overlapping occurrences of s2.

For example, if s1 is 'banana' and s2 is 'ana', your expression should return 3. 
If s1 is 'apple' and s2 is 'p', your expression should return 2.

Your answer must be a single expression that does not use square brackets (string indexing and slicing), 
and you can only call method str.find and use the arithmetic operators (+, -, etc.).

Hint: call str.find twice in your expression.

Answer:
```python

nextPoint = s1.find(s2,s1.find(s2)+1)
print(nextPoint)
```

---

###

Select the expression(s) that produce `True` when variable (code)s refers to a str that is entirely alphabetic or entirely numeric, and that produce `False` if the str is not entirely alphabetic and not entirely numeric.


```python

# 1)
s.isalpha() or s.isnumeric()

# 2)
s.isalpha() and s.isnumeric()

# 3)
s.islower() or s.isupper()

# 4)
s.lower() or s.upper() or s.isdigit()

```
Answer: 1)

---

###

Consider this code, and choose calls that results in an error
```python
def mystery(s):
    i = 0
    result = ''

    while not s[i].isdigit():
          result = result + s[i]
          i = i + 1

    return result
```

```
mystery('abc')
mystery('abc123')
mystery('123')
mystery('123abc')
```

Answer: 1)

---

###

```python
def compress_list(L):
    """ (list of str) -> list of str

    Return a new list with adjacent pairs of string elements      
     from Lconcatenated together, starting with indices 0 and 1, 2 and 3,and so on.

    Precondition: len(L) >= 2 and len(L) % 2 == 0

    >>> compress_list(['a', 'b', 'c', 'd'])
    ['ab', 'cd']
    """ 
    compressed_list = []
    i = 0

    while i < len(L):
        compressed_list.append(L[i] + L[i + 1])
        # MISSING CODE HERE
        i = i + 2

    return compressed_list
 
 
 
a = compress_list(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(a)

```


# Chapter7

### Question 1
```python
>>> d = {'a': 1, 'b': 2}
>>> # CODE MISSING HERE
>>> d
{'a': 1, 'c': 3, 'b': 2}
```

```python
d['c'] = 3
```
### Question 2

```python
>>> d = {'a': 1, 'b': 2}
>>> # CODE MISSING HERE
>>> d
{'a': 1, 'b': 3}
```

```python
d['b'] = 3
```
### Question 3

```python
>>> d = {'a': [1, 3], 'b': [5, 7]}
# CODE MISSING HERE
>>> d
{'a': [1, 2, 3], 'b': [5, 7]}
```

```python
# 1) 
d['a'] = [1,2,3]

# 2)
d['a'].insert(1,2)

# 3)
d['a'].append(2)
d['a'].sort()

```

### Question 4

```python
d = {'a': 1, 'c': 3, 'b': 2}
```

```
d = {'a': 1, 'c': 3, 'b': 2}

print('a' in d) # True
print("a" in d) # True
print(2 in d) # False

```
### Question 5

```python
d = {'a': [1, 3], 'b': [5, 7, 9], 'c': [11]}
```

```
v = len(d) - 3                      # 0
w = len(d['a' + 'c'])               # KeyError
x = len(d)                          # 3
y = len(d['a']) + len(d['c'])       # 3

```
### Question 6

```python
tup = (1, 2, 3)
```

```
print(tup[0:2] == (10, 30)) # False
tup.reverse()               # AttributeError: 'tuple' object has no attribute 'reverse'
subtup = tup[0:2]           # (1, 2)
tup[-2] = 4                 # TypeError: 'tuple' object does not support item assignment
```

### Question 7

Which one can be used as dictionary keys?

```python
['a', 'b']
('single',)
(1, 'fred', 2.0)
{1: 2, 3: 4}
```

```
d1= {['a', 'b']:1} # unhashable type: 'list'
d2={('single',):1} # {('single',): 1}
d3={(1, 'fred', 2.0):1} # {(1, 'fred', 2.0): 1}
d4={{1: 2, 3: 4}:1} # TypeError: unhashable type: 'dict'
```

### Question 8

Need to set variable total to the number of items in all the lists that occur as values in d.

In this question the answer is 5

```python
d = {1: ['a', 'b', 'c'], 2: ['d', 'e'], 3: []}
# 1)
total = 0
for k in d:
    total = total + len(d[k])

# 2)
total = 0
for k in d:
    total = total + k

# 3)        
L = []
for k in d:
    L.append(k)

total = len(L)

# 4)
L = []
for k in d:
    L.extend(d[k])

total = len(L)        

```

```
# 1)
print(total)         # 5

# 2)
print(total)         # 6
        
# 3)        
print(total)         # 3

# 4)
print(total)         # 5
```
### Question 9

```python
{1: 10, 1: 20, 1: 30}
```

```
{1: 30}
```
### Question 10

```python
L = [['apple', 3], ['pear', 2], ['banana', 3]]
d = {}
for item in L:
   d[item[0]] = item[1]
```
Populates dictionary d where each key is the first item of each inner list of L and each value is the second item of that inner list.

```
{'banana': 3, 'pear': 2, 'apple': 3}
```

### Question 11

```python
def eat(d):
    '''(dict of {str: int}) -> bool

    Each key in d is a fruit and each value is the quantity of     that fruit.

    REST OF DESCRIPTION MISSING HERE

    >>> eat({'apple': 2, 'banana': 3, 'pear': 3, 'peach': 1})
    True
    >>> eat({'apple': 0, 'banana': 0})
    False
    '''
    ate = False
    for fruit in d:
        if d[fruit] > 0:
            d[fruit] = d[fruit] - 1
            ate = True

    return ate
```

```
```
### Question 12

```python
def contains(v, d):
    ''' (object, dict of {object: list}) -> bool

    Return whether v is an element of one of the list values in    d.
    >>> contains('moogah', {1: [70, 'blue'], 2: [1.24, 'moogah'    , 90], 3.14: [80, 100]})
    True
    >>> contains('moogah', {'moogah': [1.24, 'frooble', 90], 3.    14: [80, 100]})
    False
    '''

    found = False # Whether we have found v in a list in d.

    # CODE MISSING HERE
    # 1) 
    for k in d:
        if v == k:
            found = True

    # 2) 
    for k in d:
        for i in range(len(d[k])):
            found = (d[k][i] == v)
    # 3) 
    for k in d:
        if v in d[k]:
            found = True
    # 4) 
    for k in d:
        for i in range(len(d[k])):
            if d[k][i] == v:
                found = True
    # CODE ENDING HERE
 
    return found

            
```

```
# 1)
False
True

# 2)
False
False

# 3) + 4)
True
False



```
