


# Set / List

Original
https://www.toptal.com/python/interview-questions


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
list = [ [ ] ] * 5
print(list)

list[0].append(10)
print(list)

list[1].append(20)
print(list)

list.append(30)
print(list)
```

Output
```
[[], [], [], [], []]
[[10], [10], [10], [10], [10]]
[[10, 20], [10, 20], [10, 20], [10, 20], [10, 20]]
[[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], 30]
```

**Initially I was expecting the 2nd print as below**

```
[10, [], [], [], [], []]
```


The first line of output is presumably intuitive and easy to understand; i.e.,`list = [ [ ] ] * 5` simply creates a list of 5 lists.

However, the key thing to understand here is that the statement `list = [ [ ] ] * 5` does NOT create a list containing 5 distinct lists; 
rather, it creates a a list of 5 references to the same list. 


---

