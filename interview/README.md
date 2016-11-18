
#

The site below is my reference which I frequently study .. it is wonderful and well organized.

http://www.bogotobogo.com/python/

Below is my practice note which I prepared Python technical skills

## 1) Write f() to yield list of power function

```python
for x in f(6):
    print(x, end=' ')
```

Expected output

```
0 1 4 9 16 25 
```

```python
# 1)
def f(n):
    lst = [x**2 for x in range(n)]
    return lst

# 2)
def f(n):
    for x in range(n):
        yield x**2
```
---

## 2) The difference between lists and tuples? 

```
First list are mutable while tuples are not, and second tuples can be hashed e.g. 
to be used as keys for dictionaries. 
As an example of their usage, tuples are used when the order of the elements in the sequence matters 
e.g. a geographic coordinates, "list" of points in a path or route, 
or set of actions that should be executed in specific order. 
Don't forget that you can use them a dictionary keys. For everything else use lists.
```

## 3) A few differences between Python 2.x and 3.x

```
There are many answers here but for me some of the major changes in Python 3.x are: 
all strings are now Unicode, print is now function not a statement. 
There is no range, it has been replaced by xrange which is removed. 
All classes are new style and the division of integers now returns float.
```

## 4) A 

```
To be continued
```

