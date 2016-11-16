
#

##

```python
for x in f(6):
    print(x, end=' ')
```


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
