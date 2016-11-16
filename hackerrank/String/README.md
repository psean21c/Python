
# String

### A.py : Swap Case

https://www.hackerrank.com/challenges/swap-case


__Requirement__

* Need to convert string from Upper to Lower / from Lower to Upper

```python
a = input()
for x in a:
    print(x.swapcase(), end='')
```
Input
```
HackerRank.com presents "Pythonist 2".
```

Output
```
hACKERrANK.COM PRESENTS "pYTHONIST 2".
```
---
### B.py : Mutations

https://www.hackerrank.com/challenges/python-mutations

We know lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).
Also string is immutable, but it is not easy to manipulate it whenever it is necessary.

__Requirement__

```python
# 1)
string = "abracadabra"
l = list(string)
l[5] = 'k'
string = ''.join(l)
print string

# 2)
string = "abracadabra"
string = string[:5] + "k" + string[6:]
print string
```


You will get the result below.
```
abrackdabra
```

### X.py : Find a String

https://www.hackerrank.com/challenges/find-a-string


__Requirement__

* String with substring

```python
line, target = [input() for _ in range(2)]
score = 0
for i in range(len(line)):
   if line[i:i+len(target)] == target:
        score += 1
print (score)

```




---
### X.py : name of quiz

link...

__Requirement__

* Write 

```python

```

