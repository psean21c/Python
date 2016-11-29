## Task 1
minutes_in_week = 7*24*60

## Task 2
remainder_without_mod = 2304811 -(2304811//47)*47

## Task 3
divisible_by_3 = ((673 + 909) % 3 == 0)

## Task 4
x = -9
y = 1/2
statement_val = 2**(y+1/2) if x+10<0 else 2**(y-1/2)

## Task 5
first_five_squares = { x**2 for x in {1,2,3,4,5} }

## Task 6
first_five_pows_two = { 2**x for x in {0,1,2,3,4} }

## Task 7: enter in the two new sets
X1 = { 1, 3, 5 }
Y1 = { 2, 3, 4 }

## Task 8: enter in the two new sets
X2 = { 0, 1, 2 }
Y2 = { 4, 8, 16 }

## Task 9
base = 10
digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
three_digits_set = {x*(base**2)*d1 + y*(base**1)*d2 + z*(base**0)*d3 for x in {0,1} for y in {0,1} for z in {0,1} for d1 in digits for d2 in digits for d3 in digits}

## Task 10
S = {1, 2, 3, 4}
T = {3, 4, 5, 6}
S_intersect_T = {x for x in S for y in T if x ==y}

## Task 11
L_average = sum([20, 10, 15, 75])/4 # average of: [20, 10, 15, 75]

## Task 12
LofL = [[.25, .75, .1], [-1, 0], [4, 4, 4, 4]]
LofL_sum = sum([sum(LofL[x]) for x in [0,1,2]]) # use form: sum([sum(...) ... ])

## Task 13
cartesian_product = [ [x,y] for x in {'A','B','C'} for y in {1,2,3} ] # use form: [ ... {'A','B','C'} ... {1,2,3} ... ]

## Task 14
S = {-4, -2, 1, 2, 5, 0}
zero_sum_list = [(i,j,k) for i in S for j in S for k in S if i+j+k==0]

## Task 15
exclude_zero_list = [(i,j,k) for i in S for j in S for k in S if  i + j + k == 0 and (i != 0 or j != 0 or k != 0)]

## Task 16
first_of_tuples_list = tuple([(i,j,k) for i in S for j in S for k in S if  i + j + k == 0 and (i != 0 or j != 0 or k != 0)][0])

## Task 17
L1 = [1,2,3,5,5] # <-- want len(L1) != len(list(set(L1)))
L2 = [1,2,3,5,4] # <-- same len(L2) == len(list(set(L2))) but L2 != list(set(L2))

## Task 18
odd_num_list_range = set({x for x in range(100) if x%2!=0})

## Task 19
L = ['A','B','C','D','E']
range_and_zip = list(zip([0,1,2,3,4],L))

## Task 20
list_sum_zip = [x + y for (x,y) in zip([10, 25, 40],[1, 15, 20])]

## Task 21
dlist = [{'James':'Sean', 'director':'Terence'}, {'James':'Roger', 'director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}]
k = 'James'
value_list = [dlist[x]['James'] for x in [0,1,2] ]

## Task 22
dlist = [{'Bilbo':'Ian','Frodo':'Elijah'},{'Bilbo':'Martin','Thorin':'Richard'}]
k = 'Bilbo'
value_list_modified_1 = [dlist[x]['Bilbo'] for x in [0,1]]  # <-- Use the same expression here
k = 'Frodo'
value_list_modified_2 = [dlist[x]['Frodo'] if 'Frodo' in dlist[x] else 'NOT PRESENT' for x in [0,1]] # <-- as you do here

## Task 23
square_dict = { x:x*x for x in range(100)}

## Task 24
D = {'red','white','blue'}
identity_dict = {x:x for x in D}

## Task 25
base = 10
digits = set(range(10))
representation_dict = {x*(base**2)*d1 + y*(base**1)*d2 + z*(base**0)*d3:[d1,d2,d3] for x in {0,1} for y in {0,1} for z in {0,1} for d1 in digits for d2 in digits for d3 in digits}

## Task 26
d = {0:1000.0, 1:1200.50, 2:990}
names = ['Larry', 'Curly', 'Moe']
listdict2dict = {names[i]:d[i] for i in d.keys()}

## Task 27
def nextInts(L): return [1+x for x in L]

## Task 28
def cubes(L): return [x**3 for x in L]

## Task 29
def dict2list(dct, keylist): return [y for (x,y) in zip(keylist,dct.values())]

## Task 30 
def list2dict(L, keylist): return {y:x for (x,y) in zip(L,keylist)}

