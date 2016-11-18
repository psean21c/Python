# Set

### A.py : Intro Set

https://www.hackerrank.com/challenges/py-introduction-to-sets


__Requirement__

* Use create Set() and functions - len()


```python
N = 10
S = set(list("161 182 161 154 176 170 167 171 170 174".split()))

sum = 0
for x in S:
    sum += int(x)
    
average = sum / len(S)
print(average)    

```


Output
```
169.375
```
---
### B.py : Symmetric Difference

https://www.hackerrank.com/challenges/symmetric-difference

__Requirement__

* Write 


Sample Input
```
4
2 4 5 9
4
2 4 11 12
```
Sample Output
```
5
9
11
12
```

```python
# input from hard coding
N1 = 4
S1 = set(map(int,list("2 4 5 9".split())))
N2 = 4
S2  = set(map(int,list("2 4 11 12".split())))

# input from console
N1 = int(input())
S1 = set(map(int,list(input().split())))  
N2 = int(input())
S2 = set(map(int,list(input().split())))

S3 = S1.symmetric_difference(S2)
L = list(S3)
L.sort()

for x in L:
    print(x)
 
```
### C.py : Set.add()

https://www.hackerrank.com/challenges/py-set-add

__Requirement__



input
```
7
UK
China
USA
France
New Zealand
UK
France 
```

output
```
5
```


```python
N = int(input())

S = set()

for x in range(N):
    S.add(input().strip())


print(len(S))
```
---

### D.py : pop() discard() remove()

https://www.hackerrank.com/challenges/py-set-discard-remove-pop

__Requirement__

* Write 

input
```
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5
```

output
```
4
```


```python
N = 9
S = set(map(int,"1 2 3 4 5 6 7 8 9".split()))

def moveSet(str,int):
    if str=="pop":
        S.pop()
    elif str=="remove":
        S.remove(int)
    elif str=="discard":
        S.discard(int)


Q = 10

for x in range(Q):
    c = input().strip()
    if c == "pop":
        moveSet(c,0)
    else:
        i = c.split()
        moveSet(i[0],int(i[1]))


print(sum(S))

```

### E.py : Set Mutations

https://www.hackerrank.com/challenges/py-set-mutations

__Requirement__

* Write 

input
```
16
1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
4
intersection_update 10
2 3 5 6 8 9 1 4 7 11
update 2
55 66
symmetric_difference_update 5
22 7 35 62 58
difference_update 7
11 22 35 55 58 62 66
```

output
```
38
```

```python
N1 = int(input())
S1 = set(map(int,list(input().split())))  
#print(S1)

Q = int(input())


for x in range(Q):
    c = input().split()
    #print(str(c[0]) + ": " + str(c[1]))
    S2 = set(map(int,list(input().split())))
    
    if str(c[0]) == "intersection_update":
        S1.intersection_update(S2)
    if str(c[0]) == "update":
        S1.update(S2)
    if str(c[0]) == "symmetric_difference_update":
        S1.symmetric_difference_update(S2)
    if str(c[0]) == "difference_update":
        S1.difference_update(S2)


print(sum(S1))
```





---

### X.py : name of quiz

link...

__Requirement__

* Write 

```python

```
