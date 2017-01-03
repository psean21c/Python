
#

[Original Question](https://www.hackerrank.com/challenges/zipped)

### Solution

```python
# It didn't use any zip function.
N,Q = map(int, input().strip().split(' '))

score = []
X = []
for q in range(Q):
    score = list(map(float, input().strip().split(' ')))
    X.append(score)

for n in range(N):
    midSum = 0
    for q in range(Q):
        midSum += X[q][n]
    print(round(midSum/Q,2))

```

### Approach

```python
N,Q = map(int, input().strip().split(' '))

score = []
X = []
for q in range(Q):
    score = list(map(float, input().strip().split(' ')))
    for s in score:
        print(s, end =" ")
    X.append(score)
    print()    
print()

# Print list X
print(X)
print(zip(X))
print()
 
# 3 X 5 order
for q in range(Q):
    for n in range(N):
        print(X[q][n], end =" ")
    print()
print()

# 5 X 3 order
for n in range(N):
    midSum = 0
    for q in range(Q):
        print(X[q][n], end =" ")


```

Result
```
>> input
5 3
89 90 78 93 80
90 91 85 88 86  
91 92 83 89 90.5

>> output
89.0 90.0 78.0 93.0 80.0 
90.0 91.0 85.0 88.0 86.0 
91.0 92.0 83.0 89.0 90.5 

[[89.0, 90.0, 78.0, 93.0, 80.0], [90.0, 91.0, 85.0, 88.0, 86.0], [91.0, 92.0, 83.0, 89.0, 90.5]]
<zip object at 0x0000000002661608>

89.0 90.0 78.0 93.0 80.0 
90.0 91.0 85.0 88.0 86.0 
91.0 92.0 83.0 89.0 90.5 

89.0 90.0 91.0 90.0 91.0 92.0 78.0 85.0 83.0 93.0 88.0 89.0 80.0 86.0 90.5 
```
