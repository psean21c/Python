
# Basic 

### A.py : If - else

https://www.hackerrank.com/challenges/py-if-else

__Requirement__

* Need to convert input value to integer

```python
N = int(input().strip())
```

### B.py : function

https://www.hackerrank.com/challenges/write-a-function

__Requirement__

* Write a basic function for leap day of February

### C.py : print()

https://www.hackerrank.com/challenges/python-print

__Requirement__

* Need to understand different options for print() built in function

```
Read an integer N.

Without using any string methods, try to print the following:

123..N
```

Input
```
4
```
Output
```
1234
```
### D.py : List

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

### E.py : List Comprehension

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
This is the same comprehension with different input to avoid having repetitive input calls 
```python
# 2)
x, y, z, n = (int(input()) for _ in range(4))
print ([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a + b + c != n ])
```
### F.py : List Comprehension

https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list

Input (sample-1)
```
5
2 3 6 6 5
```
Output
```
5
```

Input (sample-2)
```
4
57 57 -57 57
```
Output
```
-57
```

Below are the same ways which will save the input to the list
```python
# directly save the inputs to the list
N=int(input())
listA = [int(x) for x in input().strip().split()]

# Save the array to map first > convert them to list
N=int(input())
listA = list(map(int, input().split()))[:N]
```

1) It gave 6(not 5) and 57(not -57) because there are multiple max numbers
```python
# 1)
listA.sort()
listA.pop()
b = listA.pop()
print(b)
```

2) Beautiful power of max() !!
```python
max_value = max(listA)
while max_value == max(listA):
    listA.remove(max(listA))
max_next = max(listA)
print (max_next)
```

### G.py : List Comprehension

https://www.hackerrank.com/challenges/nested-list

__Requirement__

* Need to print the list of names who has the second lowest of grades. The key is there are more than two students who has the lowest and 2nd lowest grades.

* 성적이 두번째로 가장 낮은 학생들의 이름을 알파벳 순서대로 출력하는 문제. 문제의 핵심은 가장 성적이 안 좋은 학생과 두번째로 가장 낮은 학생들의 수가 1명 이상이 될 수 있다는 것. 

Input (sample-1)
```
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
```
Output
```
Berry
Harry
```
Input (sample-2)
```
5
Harsh
20
Beria
20
Varun
19
Kakunami
19
Vikas
21
```
Output
```
Beria
Harsh
```

__GSolutionbyDrJang.py__
* Different solution wrtten by __Dr. DongWook Jang__

* Originally created in Python 2 and converted to Python 3 by __Simon Park__

__GSolutionbyCalgary.py__
* Different solution wrtten by __Eugene Kim__


### H.py : Finding the percentage

https://www.hackerrank.com/challenges/finding-the-percentage

* Need to utilize list in more dynamic ways

Input
```
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
```
Output
```
56.00
```

How to use the format : 56.00

```python
print('{0:.2f}'.format(dic[name]))
```

# Built In function in Python3
![pybuiltin](https://cloud.githubusercontent.com/assets/5623445/20272862/438a0cf4-aa5d-11e6-852d-fc12a416c85b.PNG)

There are 68 built in functions in Python 3 but it is challenging to master each function 

* isinstance

isinstance("this is a string", str) will return True

https://docs.python.org/3/tutorial/index.html

https://docs.python.org/3/library/intro.html

