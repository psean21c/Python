


# Set

Original
https://www.toptal.com/python/interview-questions


### A.py : extendedList


__Requirement__

* Need to convert string from Upper to Lower / from Lower to Upper

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
### X.py : name of quiz

link...

__Requirement__

* Write 

```python

```
