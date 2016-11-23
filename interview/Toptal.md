


# Set / List

Original
https://www.toptal.com/python/interview-questions

### List: Comprehension

__Requirement__

* Need to write Comprehension

Given a list of N numbers, use a single list comprehension to produce a new list that only contains those values that are:

(a) even numbers, and

(b) from elements in the original list that had even indices

For example, if list[2] contains a value that is even, that value should be included in the new list, since it is also at an even index (i.e., 2) in the original list. 
However, if list[3] contains an even number, that number should not be included in the new list since it is at an odd index (i.e., 3) in the original list.

Solution
```python
list = [ 1 , 3 , 5 , 8 , 10 , 13 , 18 , 36 , 78 ]
print([x for x in list[::2] if x%2 == 0])
```

```
[10, 18, 78]
```

---
### Class: Inheritance

__Requirement__

* Need to understand class variables

```python
class Parent(object):
    x = 1

class Child1(Parent):
    pass

class Child2(Parent):
    pass

print (Parent.x, Child1.x, Child2.x)
Child1.x = 2
print (Parent.x, Child1.x, Child2.x)
Parent.x = 3
print (Parent.x, Child1.x, Child2.x)

```
What's result? 
```
1 1 1
1 2 1
3 2 3
```

The key to the answer is that, in Python, class variables are internally handled as dictionaries. If a variable name is not found in the dictionary of the current class, the class hierarchy (i.e., its parent classes) are searched until the referenced variable name is found (if the referenced variable name is not found in the class itself or anywhere in its hierarchy, an AttributeError occurs).

---

### List: Comprehension of List

__Requirement__

* Need to understand generator / clouser (late binding)
```python
def multiply(n):
  return [lambda x : i * x for i in range(n)]

def printL(lst):
  for l in lst:
    print(str(l) + " ", end="")

a = [i(2) for i in multiply(5)]
printL(a)
```

What's result? 
```
[8, 8, 8, 8, 8]
```
The output of the above code will be `[8, 8, 8, 8, 8]` not `[0, 2, 4, 6, 8]`

The reason for this is that Python’s closures are late binding. This means that the values of variables used in closures are looked up at the time the inner function is called. So as a result, when any of the functions returned by multiply() are called, the value of i is looked up in the surrounding scope at that time. By then, regardless of which of the returned functions is called, the for loop has completed and i is left with its final value of 4. Therefore, every returned function multiplies the value it is passed by 4, so since a value of 2 is passed in the above code, they all return a value of 6 (i.e., 4 x 2).

Solution-1: generator
```python
def multiply(n):
  for i in range(n):
    yield lambda x: i * x
```

Solution-2:  create a closure that binds immediately to its arguments by using a default argument
```python
def multiply(n):
  return [lambda x, i=i : i * x for i in range(n)]
```

---

### List: index of List

__Requirement__

* Need to understand list of lists
```python
lst = ['a', 'b', 'c', 'd', 'e']

print(lst[10:])
```

What's result? `IndexError` or `[]`


According to 
[API for List](https://docs.python.org/3.6/library/stdtypes.html#sequence-types-list-tuple-range)

`s[i:j]` : slice of s from i to j

![list](https://cloud.githubusercontent.com/assets/5623445/20571694/88b0e990-b176-11e6-87c2-ffd4a38ba378.PNG)

But it is tricky because the range is different when the `index` is `[index:]` and `[:index]`
```
lst=['a', 'b', 'c', 'd', 'e']
lst[2:] = ['c', 'd', 'e']
lst[:2] = ['a', 'b']
```

---


### List: extend List


__Requirement__

* Need to understand default value of [empyt list] for parameter of the function

```python
def extendList(val, list=[]):
    list.append(val)
    return list


list1 = extendList(10)
print ("list1 = %s" % list1)

list2 = extendList(123,[])
print ("list2 = %s" % list2)

list3 = extendList('a')
print ("list1 = %s" % list1)
print ("list2 = %s" % list2)
print ("list3 = %s" % list3)

```

Output
```
list1 = [10]

list2 = [123]

list1 = [10, 'a']
list2 = [123]
list3 = [10, 'a']
```

**Initially I was expecting list1 didn't have 'a' **

what actually happens is that the new default list is created only once when the function is defined, 
and that same list is then used subsequently whenever extendList is invoked without a list argument being specified. 
This is because expressions in default arguments are calculated when the function is defined, not when it’s called.

list1 and list3 are therefore operating on the same default list, 
whereas list2 is operating on a separate list that it created 
(by passing its own empty list as the value for the list parameter).


```python
def extendList(val, list=None):
  if list is None:
    list = []
  list.append(val)
  return list
```

With this revised implementation, the output would be:

Output
```
list1 = [10]

list2 = [123]

list1 = [10]
list2 = [123]
list3 = [10]
```

---
### List: List of Lists

__Requirement__

* Need to understand list of lists

```python
lst1 = [[] for i in range(3)]
print(lst1)

lst1[0].append(3)
print(lst1)

lst1[1].append(5)
print(lst1)

lst1[2].append(7)
print(lst1)

print()

lst2 = [ [ ] ] * 3
print(lst2)

lst2[0].append(3)
print(lst2)

lst2[1].append(5)
print(lst2)

lst2[1].append(7)
print(lst2)
```

Output
```
[[], [], []]
[[3], [], []]
[[3], [5], []]
[[3], [5], [7]]

[[], [], []]
[[3], [3], [3]]
[[3, 5], [3, 5], [3, 5]]
[[3, 5, 7], [3, 5, 7], [3, 5, 7]]

```

**Initially I was expecting the 2nd print as ** `[3, [], [], []]`  * or * `[[3], [], []]`



What happens is that the first line of output is presumably intuitive and easy to understand; `list = [ [ ] ] * 5` simply creates a list of 5 lists.

However, the key thing to understand here is that the statement `list = [ [ ] ] * 5` does NOT create a list containing 5 distinct lists; 
rather, it creates a a list of 5 references to the same list. 


---


### Reference

[link to Python 3 API](https://docs.python.org/3.6/library/stdtypes.html#sequence-types-list-tuple-range)

[link to GitHub MarkDown](https://guides.github.com/features/mastering-markdown/)

[link to HitchHiker's Python](http://docs.python-guide.org/en/latest/writing/gotchas/)

