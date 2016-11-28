
# Always be prepared


Below is my practice note which I prepared Python technical skills

## Print Directory + files 

```python
def print_directory_contents(sPath):
    """
    This function takes the name of a directory 
    and prints out the paths files within that 
    directory as well as any files contained in 
    contained directories. 

    This function is similar to os.walk. Please don't
    use os.walk in your answer. We are interested in your 
    ability to work with nested structures. 
    """
    # MISSING CODE
    
```

Answer
```python
	for child in os.listdir(sPath): 
		print(child)
		childPath = os.path.join(sPath,child)
		if os.path.isdir(childPath):
			print_directory_contents(childPath)
		else: 
			print(childPath)
```


---
## Write f() to yield list of power function

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

## The difference between lists and tuples? 

```
First list are mutable while tuples are not, 
and second tuples can be hashed to be used as keys for dictionaries. 

As an example of their usage, tuples are used when the order of the elements in the sequence matters 
e.g. a geographic coordinates, "list" of points in a path or route, 
or set of actions that should be executed in specific order. 

Don't forget that you can use them a dictionary keys. For everything else use lists.
```

---
## A few differences between Python 2.x and 3.x

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

---


[보고 또 보고](http://www.bogotobogo.com/python/)

[Code Mentor Python](https://www.codementor.io/python/tutorial/essential-python-interview-questions)
