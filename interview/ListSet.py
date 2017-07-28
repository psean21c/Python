

import timeit

NB_ITEMS = 1000000
NB_LOOKUP = 10000

mylist = range(NB_ITEMS)
myset = set(mylist)

def test_list():
    for i in range(NB_LOOKUP):
        10000 in mylist

def test_set():
    for i in range(NB_LOOKUP):
        10000 in myset

print timeit.timeit(test_list, number=10)

print timeit.timeit(test_set, number=10)

'''
21.8953108788
0.0142509937286
'''
