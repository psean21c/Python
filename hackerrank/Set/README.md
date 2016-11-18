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


---
### X.py : name of quiz

link...

__Requirement__

* Write 

```python

```
