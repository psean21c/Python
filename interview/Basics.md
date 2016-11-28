
### map()

map executes the function given as the first argument on all the elements of the iterable given as the second argument.

__Requirement__

* Need to understand the function of `map`


```python
results = ['1', '2', '3']

# 1) 
print(results)

# 2) after map()
results = map(int, results) 
print(results)

# 3) iterable print
for x in results:
    print(x, end= " ")
    
```

output
```
['1', '2', '3']
<map object at 0x000000000048E588>
1 2 3 
```



---

### enumerate()

```python
ints = [8, 23, 45, 12, 78]
for idx, val in enumerate(ints): print(idx, val)
```

output
```
0 8
1 23
2 45
3 12
4 78
```

---

### The difference between lists and tuples? 

```
First list are mutable while tuples are not, 
and second tuples can be hashed to be used as keys for dictionaries. 

As an example of their usage, tuples are used when the order of the elements in the sequence matters 
e.g. a geographic coordinates, "list" of points in a path or route, 
or set of actions that should be executed in specific order. 

Don't forget that you can use them a dictionary keys. For everything else use lists.
```

---
### A few differences between Python 2.x and 3.x

```
There are many answers here but for me some of the major changes in Python 3.x are: 
all strings are now Unicode, print is now function not a statement. 
There is no range, it has been replaced by xrange which is removed. 
All classes are new style and the division of integers now returns float.
```

---

### What is a docstring?

```python
def f(n):
	return n + 1



print(f.__doc__)
```
It will print 'None' as below
```
None
```

In order to see the function's documentation, you need to add comments below the function with proper indentation
```python
def f(n):
    '''int -> int
This function does blar blar
    '''
	return n + 1

print(f.__doc__)
```

It will print the documentation string for a function

```
int -> int
This function does blar blar
```
