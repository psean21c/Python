
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
