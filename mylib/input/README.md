
### Situation

# Different format of inputs.

It is different when you have two inputs from one line and two lines
```python
2 3
```


```python
2
3
```

```python
# 2)
x = int(input())
y = int(input())

# 1)
X =[int(a) for a in input().strip().split()]
N,M = X
```

In order to read inputs below
```
4 3
90
180
270
```
3 means there are 3 lines below..

```python
n,q = input().strip().split(' ')
n,q = [int(n),int(q)]
for a0 in range(q):
    angle = int(input().strip())
```
---

### Requirement

* Save separated values into dictionary right after reading the line()
* Read next line until no line exists

input
```
3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry
```
output
```
sam=99912222
Not found
harry=12299933
```

```python
n = int(input())
name_numbers = [input().split() for _ in range(n)]
phone_book = {k: v for k,v in name_numbers}
while True:
    try:
        name = input()
        if name in phone_book:
            print('%s=%s' % (name, phone_book[name]))
        else:
            print('Not found')
    except:
        break
```
