
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
### X.py : name of quiz

link...

__Requirement__

* Write 

```python

```

