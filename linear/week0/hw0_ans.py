## Problem 1
def myFilter(L, num): return [x for x in L if x%num !=0]

## Problem 2
def myLists(L): return [list(range(1,i+1)) for i in L]

## Problem 3
def myFunctionComposition(f, g): return {x:v for (x,y) in zip(f.keys(),f.values()) for (z,v) in zip(g.keys(),g.values()) if y == z }

## Problem 4
# Please only enter your numerical solution.

complex_addition_a = (3 + 1j) + (2 + 2j)
complex_addition_b = (-1 + 2j) + (1 - 1j)
complex_addition_c = (2 + 0j) + (-3 + 0.001j)
complex_addition_d = 4*(0 + 2j) + (0.001 + 1j)

## Problem 5
GF2_sum_1 = 1 ^ 1 ^ 1 ^ 0
GF2_sum_2 = (1 & 1) ^ ( 0 & 1)  ^ (0 & 0) ^ (1 & 1)
GF2_sum_3 = (1 ^ 1 ^ 1) & (1 ^ 1 ^ 1 ^ 1)


## Problem 6
def mySum(L): return sum(L)

## Problem 7
def myProduct(L):
    r = 1
    for i in L:
        r *= i
    return r

## Problem 8
def myMin(L): return min(L)

## Problem 9
def myConcat(L):
    concat = ''
    for i in L:
        concat = concat + i
    return concat


## Problem 10
def myUnion(L):
    union = set()
    for i in L:
        union = union | i
    return union
