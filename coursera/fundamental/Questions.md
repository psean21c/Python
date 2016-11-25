
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
