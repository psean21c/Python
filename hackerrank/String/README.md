
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
---
### C.py : Find a String

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
### D.py : String Validators

https://www.hackerrank.com/challenges/string-validators

__Requirement__

* Output Format
```
In the first line, print True if S has any alphanumeric characters. Otherwise, print False. 
In the second line, print True if S has any alphabetical characters. Otherwise, print False. 
In the third line, print True if S has any digits. Otherwise, print False. 
In the fourth line, print True if S has any lowercase characters. Otherwise, print False. 
In the fifth line, print True if S has any uppercase characters. Otherwise, print False.
```

Input
```
123
```
Output
```
True
False
True
False
False
```

It is important to know basics - this case any() function to save your effort.

---
### E.py : StringFormatting

https://www.hackerrank.com/challenges/python-string-formatting

__Requirement__

1) Decimal

2) Octal

3) Hexadecimal (capitalized)

4) Binary

If you provide 17 to input() it will produce the result as below

```
    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001
```

```python

N = int(input())
pad = len(format(N,'b'))
for i in range(N):
    numa = str(i+1).rjust(pad)
    octa = str(format(i+1, 'o')).rjust(pad)
    hexa = str(format(i+1, 'x')).upper().rjust(pad)
    bina = str(format(i+1, 'b')).rjust(pad)
    print( numa + " " + octa + " " + hexa + " " + bina)
```

### F.py : Alphabet Rangoli

https://www.hackerrank.com/challenges/alphabet-rangoli

__Requirement__

* Write 

```
#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------
```


```python
# Version 1

import string
x = int(input())
my_range = list(range(1,x+1)) + list(range(x-1,0,-1))
for i in my_range:
    n = x
    my_row = []
    for j in range(1,2*i):            
        if j <= i:
            n = n-1
        else:           
            n = n+1
        my_row.append(string.ascii_lowercase[n])
    print("-".join(my_row).center((4*x)-3,"-"))

# Version 2
n = int(input())
print("\n".join(map(lambda i: "-".join(map(lambda j: chr(97 + abs(i) + abs(j)), range(abs(i) - n + 1, n - abs(i)))).center(4 * n - 3, "-"), range(-n + 1, n))))

```

---
### X.py : name of quiz

link...

__Requirement__

* Write 

```python

```

