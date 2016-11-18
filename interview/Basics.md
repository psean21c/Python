
### map()


__Requirement__

* Need to convert from string to int in list / set

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
