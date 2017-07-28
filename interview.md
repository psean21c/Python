

''' python
import timeit

NB_ITEMS = 100000

def test_list():
    x = []
    for i in range(NB_ITEMS):
        x.append(i)

def test_set():
    x = set([])
    for i in range(NB_ITEMS):
        x.add(i)

print timeit.timeit(test_list, number=10)

print timeit.timeit(test_set, number=10)

0.154641866684
0.184559106827


# from time import time

# x = []
# t0 = time()
# for i in range(NB_ITEMS):
#     x.append(i)
# print ("list: %s" % (time() - t0))
#
#
#
# y = set([])
# t1 = time()
# for i in range(NB_ITEMS):
#     y.add(i)
# print 'set: %s' % (time() - t1)




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


21.8953108788
0.0142509937286
'''
