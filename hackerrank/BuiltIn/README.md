
### Basic 

# A.py : If - else

https://www.hackerrank.com/challenges/py-if-else

Need to convert input value to integer
```python
N = int(input().strip())
```

# B.py : function

Write function for leap day of February

# C.py : print()

Need to understand different options for print() built in function

Read an integer N.

Without using any string methods, try to print the following:

123..N

Input
```
4
```
Output
```
1234
```
# D.py : List

https://www.hackerrank.com/challenges/python-lists

Input
```
12
insert 0 5
insert 1 10
insert 0 6
print 
remove 6
append 9
append 1
sort 
print
pop
reverse
print
```
Output
```
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
```

# E.py : List Comprehension

https://www.hackerrank.com/challenges/list-comprehensions

Input
```
1
1
1
2
```
Output
```
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]] 
```

Below is a Python comprehension which will produce the output with one shot

```python
# 1)
x, y, z, n = int(input()), int(input()), int(input()), int(input())
print ([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a + b + c != n ])
```
This is the same comprehension with different 
```python
# 2)
x, y, z, n = (int(input()) for _ in range(4))
print ([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a + b + c != n ])
```


### Built In function in Python3
![pybuiltin](https://cloud.githubusercontent.com/assets/5623445/20272862/438a0cf4-aa5d-11e6-852d-fc12a416c85b.PNG)

https://docs.python.org/3/tutorial/index.html

https://docs.python.org/3/library/intro.html

