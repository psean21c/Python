
### Lists vs Sets
```python
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
```

### Objects
```python
class MyClass(object):

    def __init__(self, x):
        self.x = x

    def returns_double(self):
        return self.x * 2

class MyClass2(MyClass):
    def returns_triple(self):
        return self.x * 3


myobject = MyClass(2)
print (myobject.x)
print (myobject.returns_double())

myobject2 = MyClass2(3)

print (myobject2.returns_triple())

myobject3 = myobject

print (myobject is myobject2) # False
print (myobject is myobject3)  # True

print (isinstance(myobject, MyClass)) # True
print (isinstance(myobject, MyClass2)) # False
print (isinstance(myobject2, MyClass2)) # True
print (isinstance(myobject2, MyClass)) # True
```

### Methods in OOP
```python

from random import choice
from time import sleep


MOODS = ['relaxed','inquisitive','grumpy']
class Cat(object):

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.mood = choice(MOODS)

    def __str__(self):
        return 'My name is %s' % (self.name)

    def ask_food(self):
        return 'More food please'

    def get_mood(self):
        self.mood = choice(MOODS)


cat1 = Cat('Tiger','blue')
print (cat1)
print (cat1.name)

cat2 = Cat('Fuma','white')
cat3 = Cat('Lion','green')

cats = [cat1,cat2,cat3]

print [cat for cat in cats] # Will not use the __str__ representation

print [str(cat) for cat in cats]

print [cat.name for cat in cats]

print [cat.name for cat in cats if cat.color == 'white']

print cat1.ask_food()

print [(cat.name, cat.ask_food(), cat.get_mood()) for cat in cats]

print cat1.mood

while True:
    for cat in cats:
        cat.get_mood()
        print '%s : %s' % (cat.name, cat.mood)
    sleep(2)

```

### comprehensions

'''python


# List
output_list = []
for x in range(10):
    output_list.append(x**2)

print output_list

output_list2 = [x**2 for x in range(10)]
print output_list2

# Set
output_set = set([])
for x in range(10):
    output_set.add(x**2)

print output_set

#output_set2 = {x**2 for x in range(10)} # python 2.6 not support set comprehension
#print output_set2


# a dictionary
my_dict = {}
for x in range(10):
    my_dict[x] = x**2

print my_dict

my_dict2 = {x: x**2 for x in range(10)}
print my_dict2
'''
