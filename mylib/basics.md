
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
### list

```python
#lst = ([10, 2, 5], [7, 1, 0], [9, 9, 9], [1, 23, 12], [6, 5, 9])
sorted(lst, key=itemgetter(1))

# You are expecting to see the 2nd line, 
# but it's not unless you assing it to another list object
[[10, 2, 5], [7, 1, 0], [9, 9, 9], [1, 23, 12], [6, 5, 9]]
[[7, 1, 0], [10, 2, 5], [9, 9, 9], [6, 5, 9], [1, 23, 12]]

# Assign it to lst2
lst2 = sorted(lst, key=itemgetter(1))
print(lst2)
[[7, 1, 0], [10, 2, 5], [9, 9, 9], [6, 5, 9], [1, 23, 12]]

```



---
### filter()


```python
mult1 = filter(lambda x: x % 3 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(mult1)

for i in mult1:
    print(i, end=" ")

```
If you print mult1, it doesn't directly give you the values, Instead it will show object address.
```
<filter object at 0x000000000069E668>
3 6 9 
```

```python
mult2 = list(filter(lambda x: x % 3 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(mult2)

for i in mult2:
    print(i, end=" ")  

```
If you embrace it with list after filter(), it will be different.
```
[3, 6, 9]
3 6 9 
```


---
### join() + split()

Need to understand the return type of split() and join()
```python
'''
input/output
hello world
>>
Hello World

'''

def capitalize(string):
    pass

if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)
    
```
Solution
```python
def capitalize(string):
#     for a in string.split():
#         print(a)
#    print(' '.join(a.capitalize() for a in string.split()))
    re = ' '.join(a.capitalize() for a in string.split())
    return re
```
if you print the method after calling the method ...
```python
def capitalize(string):
    print(a.capitalize() for a in string.split())
```
You will be seeing object not the string.
```
<generator object <genexpr> at 0x000000000283B6C0>
None
```

It is different 

```
    return ' '.join(a.capitalize() for a in string.split(' '))  # 1)
    return ' '.join(a.capitalize() for a in string.split())     # 2)
    
 s d f g h j  k l z   # input
 S D F G H J  K L Z   # 1)
 S D F G H J K L Z    # 2) remove one space if there are twos
 
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
Secondly tuples can be hashed to be used as keys for dictionaries. 

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

### String Format

https://pyformat.info/
