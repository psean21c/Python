

### Question 1
```python
>>> d = {'a': 1, 'b': 2}
>>> # CODE MISSING HERE
>>> d
{'a': 1, 'c': 3, 'b': 2}
```

```
d['c'] = 3
```
### Question 2

```python
>>> d = {'a': 1, 'b': 2}
>>> # CODE MISSING HERE
>>> d
{'a': 1, 'b': 3}
```

```
d['b'] = 3
```
### Question 3

```python
>>> d = {'a': [1, 3], 'b': [5, 7]}
# CODE MISSING HERE
>>> d
{'a': [1, 2, 3], 'b': [5, 7]}
```

```
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
 
    return found

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



