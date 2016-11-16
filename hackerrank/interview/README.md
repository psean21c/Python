
#


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

## 2)

