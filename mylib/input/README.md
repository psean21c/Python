
# Situation

### Different format of inputs.

It is different when you have two inputs from one line and two lines

```python
# 1)
2 3
```


```python
# 2)
2
3
```

```python
# 1)
# It will give error when you provide input data as 2)
X =[int(a) for a in input().strip().split()]
N,M = X


# 2)
# It will give error when you provide input data as 1)
x = int(input())
y = int(input())

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
# 1)
N,Q = input().strip().split(' ')
N,Q = [int(N),int(Q)]
# Without int(N), it will give error - not convert from str to int

# 2) Or you can map after converting to int
N,Q = map(int,input().strip().split(' '))

for q in range(Q):
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
