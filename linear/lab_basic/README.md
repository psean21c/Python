
## Task 1

Use Python to find the number of minutes in a week.
```python
minutes_in_week = ...
```

## Task 2

Task 2: Use Python to find the remainder of 2304811 divided by 47 without using the modulo operator %.
(Hint: Use //.)

```python
remainder_without_mod = ...
```


## Task 3

Enter a Boolean expression to test whether the sum of 673 and 909 is divisible by 3.

```python
divisible_by_3 = ...
```

## Task 4

Assign the value -9 to x and 1/2 to y. Predict the value of the following expression, then enter it to check your prediction:

`2**(y+1/2) if x+10<0 else 2**(y-1/2)`

```python
x = -9
y = 1/2
statement_val = ...
```

## Task 5

Write a comprehension over {1,2,3,4,5} whose value is the set consisting of the squares of the first five positive integers.

```python
first_five_squares = { ... for _ in {1,2,3,4,5} }

```


## Task 6

Write a comprehension over {0,1,2,3,4} whose value is the set consisting of the first five powers of two, starting with 2^0.

```python
first_five_pows_two = { ... for _ in {0,1,2,3,4} }

```


## Task 7: enter in the two new sets

The value of the previous comprehension, {x*y for x in {1,2,3} for y in {2,3,4}}, is a seven-element set. 

Replace {1,2,3} and {2,3,4} with two other three-element sets so that the value becomes a nine-element set.

```python

```



## Task 8: enter in the two new sets

Replace {1,2,3} and {2,3,4} in the previous comprehension with two disjoint (i.e. non-overlapping) three-element sets 
so that the value becomes a five-element set.

```python
X2 = { ..., ..., ... }
Y2 = { ..., ..., ... }

```

## Task 9

Assign 10 to the variable base. Assign the set {0,1,2,3,4,5,6,7,8,9} to the variable digits.
Now write an expression using a comprehension and base and digits whose value is the set of all at-most-three-digit numbers.
Your expression should work for any base. For example, if you instead assign 2 to base and assign {0,1} to digits, 
the value of your expression should be {0,1,2,3,4,5,6,7} because this is the set of numbers that, base two, have at most three digits.

```python
base = 10
digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
three_digits_set = { ... }

```
## Task 10

Assume that S and T are assigned sets. Without using the intersection operator &, 
write a comprehension over S whose value is the intersection of S and T. Hint: Use a membership test in a filter at the end of the comprehension.

Try out your comprehension with S = {1,2,3,4} and T = {3,4,5,6}.

```
X1 = { ..., ..., ... }
Y1 = { ..., ..., ... }
```

```python
S = {1, 2, 3, 4}
T = {3, 4, 5, 6}
S_intersect_T = { ... }
```


## Task 11

Write an expression whose value is the average of the elements of the list [20, 10, 15, 75].

```python
L_average = ... # average of: [20, 10, 15, 75]

```


## Task 12

Assign to the variable LofL the list of lists [[.25, .75, .1], [-1, 0], [4, 4, 4, 4]].
Using a comprehension, write an expression involving LofL that returns the sum of all the numbers in all three lists. 
The expression has the form sum([sum(....
```python
LofL = [[.25, .75, .1], [-1, 0], [4, 4, 4, 4]]
LofL_sum = ... # use form: sum([sum(...) ... ])

```

## Task 13

Write a double list comprehension over the lists ['A','B','C'] and [1,2,3] whose value is the
list of all possible two-element lists [letter, number]. That is, the value is
```
[['A', 1], ['A', 2], ['A', 3], ['B', 1], ['B', 2],['B', 3],['C', 1], ['C', 2], ['C', 3]]

```

```python
cartesian_product = ... # use form: [ ... {'A','B','C'} ... {1,2,3} ... ]

```



## Task 14

Suppose S is a set of integers, e.g. f{-4, -2, 1, 2, 5, 0}. Write a triple comprehension whose value
is a list of all three-element tuples (i, j, k) such that i, j, k are elements of S whose sum is zero.

```python
S = {-4, -2, 1, 2, 5, 0}
zero_sum_list = [ ... ] 

```

## Task 15

Modify the comprehension of the previous task so that the resulting list does not include (0, 0, 0).
Hint: add a filter.

```python
exclude_zero_list = [ ... ]

```
## Task 16

Further modify the expression so that its value is not the list of all such tuples but is the first
such tuple.

```python
first_of_tuples_list = ...
```

## Task 17

Find an example of a list L such that len(L) and len(list(set(L))) are different. 
Then find a list L such that len(L) and len(list(set(L))) are the same but the order of elements differs between L and list(set(L)).

```python
L1 = [...] # <-- want len(L1) != len(list(set(L1)))
L2 = [...] # <-- same len(L2) == len(list(set(L2))) but L2 != list(set(L2))
```

## Task 18

Write a comprehension over a range of the form range(n) 
such that the value of the comprehension is the set of odd numbers from 1 to 99.

```python
odd_num_list_range = {...}

```

## Task 19

Assign to L the list consisting of the first five letters ['A','B','C','D','E']. 
Next, use L in an expression whose value is [(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D'), (4, 'E')]. Your expression
should use a range and a zip, but should not use a comprehension.

```python
L = ['A','B','C','D','E']
range_and_zip = ...

```

## Task 20

Starting from the lists [10, 25, 40] and [1, 15, 20], write a comprehension whose value is
the three-element list in which the first element is the sum of 10 and 1, the second is the sum of 25 and 15,
and the third is the sum of 40 and 20. Your expression should use zip but not list.


```python
list_sum_zip = [...]

```

## Task 21

Suppose dlist is a list of dictionaries and k is a key that appears in all the dictionaries in dlist.
Write a comprehension whose value is the list whose ith element is the value corresponding to key k in the i-th dictionary in dlist.
Test your comprehension with some data. Here are some example data.
```
dlist = [{'James':'Sean', 'director':'Terence'}, {'James':'Roger','director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}]
k = 'James'
```

```python
dlist = [{'James':'Sean', 'director':'Terence'}, {'James':'Roger', 'director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}]
k = 'James'
value_list = [...]

```

## Task 22

Modify the comprehension in Task 21 to handle the case in which k might not appear in all the
dictionaries. The comprehension's value is the list whose ith element is the value corresponding to key k in
the ith dictionary in dlist if that dictionary contains that key, and 'NOT PRESENT' otherwise.
Test your comprehension with k = 'Bilbo' and k = 'Frodo' and with the following list of dictionaries:
dlist = [{'Bilbo':'Ian','Frodo':'Elijah'},{'Bilbo':'Martin','Thorin':'Richard'}]

```python
dlist = [{'Bilbo':'Ian','Frodo':'Elijah'},{'Bilbo':'Martin','Thorin':'Richard'}]
k = 'Bilbo'
value_list_modified_1 = [...] # <-- Use the same expression here
k = 'Frodo'
value_list_modified_2 = [...] # <-- as you do here

```

## Task 23

Using range, write a comprehension whose value is a dictionary. The keys should be the integers
from 0 to 99 and the value corresponding to a key should be the square of the key.

```python
square_dict = {...}

```

## Task 24
Task 24: Assign some set to the variable D, e.g. D ={'red','white','blue'}. Now write a comprehen-
sion whose value is a dictionary that represents the identity function on D.

```python
D = {'red','white','blue'}
identity_dict = {...}

```

## Task 25

Using the variables base=10 and digits=set(range(10)), write a dictionary comprehension
that maps each integer from 0 through 999 to the list of three digits that represents that integer in base 10.
That is, the value should be

```
{0: [0, 0, 0], 1: [0, 0, 1], 2: [0, 0, 2], 3: [0, 0, 3], ...,
10: [0, 1, 0], 11: [0, 1, 1], 12: [0, 1, 2], ...,
999: [9, 9, 9]}
```

Like Task 9, your expression should work for any base. For example, if you instead assign 2 to base and
assign {0,1} to digits, the value should be
```
{0: [0, 0, 0], 1: [0, 0, 1], 2: [0, 1, 0], 3: [0, 1, 1],..., 7: [1, 1, 1]}
```

```python
base = 10
digits = set(range(10))
representation_dict = {...}

```

## Task 26

Suppose d is a dictionary that maps some employee IDs (a subset of the integers from 0 to n􀀀1)
to salaries. Suppose L is an n-element list whose ith element is the name of employee number i. Your goal is
to write a comprehension whose value is a dictionary mapping employee names to salaries. You can assume
that employee names are distinct. However, not every employee ID is represented in d.
Test your comprehension with the following data:
```
d = {0:1000.0, 3:990, 1:1200.50}
L = ['Larry', 'Curly', '', 'Moe']
```

```python
d = {0:1000.0, 1:1200.50, 2:990}
names = ['Larry', 'Curly', 'Moe']
listdict2dict = { ... }

```

## Task 27

Define a one-line procedure nextInts(L) specified as follows:
```
* input: list L of integers
* output: list of integers whose ith element is one more than the ith element of L
```
* example: input [1, 5, 7], output [2, 6, 8].

```python
def nextInts(L): return [ ... ]

```

## Task 28

Define a one-line procedure cubes(L) specified as follows:
```
* input: list L of numbers
* output: list of numbers whose ith element is the cube of the ith element of L
* example: input [1, 2, 3], output [1, 8, 27].
```

```python
def cubes(L): return [ ... ] 

```

## Task 29

Define a one-line procedure dict2list(dct,keylist) with this spec:
```
* input: dictionary dct, list keylist consisting of the keys of dct
* output: list L such that L[i] = dct[keylist[i]] for i = 0, 1, 2, ... , len(keylist) - 1
* example: input dct={'a':'A', 'b':'B', 'c':'C'} and keylist=['b','c','a'], 
output ['B', 'C', 'A']
```

```python
def dict2list(dct, keylist): return [ ... ]

```

## Task 30 

Define a one-line procedure list2dict(L, keylist) specified as follows:
```
* input: list L, list keylist of immutable items
* output: dictionary that maps keylist[i] to L[i] for i = 0, 1, 2,... , len(L) - 1
* example: input L=['A','B','C'] and keylist=['a','b','c'], output {'a':'A', 'b':'B', 'c':'C'}
```
Hint: Use a comprehension that iterates over a zip or a range.

```python
def list2dict(L, keylist): return { ... } 

```

