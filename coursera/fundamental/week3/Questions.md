
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

```pyhton

nextPoint = s1.find(s2,s1.find(s2)+1)
print(nextPoint)

'''
