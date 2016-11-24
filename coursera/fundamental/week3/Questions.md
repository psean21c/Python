

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


