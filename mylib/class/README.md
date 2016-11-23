#


###

```python
class Topo:
  def __init__(self,address,name):
    print('Topo')
    self.address = address
    self.name = name

topo1 = Topo('New York','t1')
print(topo1.address + ",name=" + str(topo1.name))

topo2 = Topo('Chicago')
print(topo2.address + ",name=" + str(topo2.name))
```

output
```
Topo
New York,name=t1
Traceback (most recent call last):
  File "C:\D-Drive\Lab\Python\mapr\A.py", line 10, in <module>
    topo2 = Topo('Chicago')
TypeError: __init__() missing 1 required positional argument: 'name'
```


In order to avoid having this problem, you can add 'None' as a default value to name.

```python
class Topo:
  def __init__(self,address,name=None):
    print('Topo')
    self.address = address
    self.name = name

topo1 = Topo('New York','t1')
print(topo1.address + ",name=" + str(topo1.name))

topo2 = Topo('Chicago')
print(topo2.address + ",name=" + str(topo2.name))
```

output
```
Topo
New York,name=t1
Topo
Chicago,name=None
```

### Inheritance

```python

class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def area(self):
        return self.x * self.y
		
class Square(Shape):
    def __init__(self,x):
        self.x = x
        self.y = x
        print('<init>Square: x=',self.x,',y=',self.y)
    def squared(self):
        return self.x * self.y


class DoubleSquare(Square):
    def __init__(self,y):
        self.x = 2 * y
        self.y = y
        print('<init>DoubleSquare:x=',self.x,',y=',self.y)
    def perimeter(self):
        return 2 * self.x + 3 * self.y
		

square1 = Shape(10, 20)
print ("square1 area:x=",square1.x,",y=",square1.y)
square2 = Square(30)
print ("square2 area:x=",square2.x,",y=",square2.y,",area=",square2.area(),",squared=",square2.squared())


dict1 = {}


# Then, create some instances of classes in the dictionary:
dict1["DoubleSquare"] = DoubleSquare(5)
dict1["LongRectangle"] = Shape(10,20)


#You can now use them like a normal class:
print ('DoubleSquare =',dict1["DoubleSquare"].area(),',perimeter=',dict1["DoubleSquare"].perimeter())
print ('LongRectangle =',dict1["LongRectangle"].area())

```
Output
```
square1 area:x= 10 ,y= 20
<init>Square: x= 30 ,y= 30
square2 area:x= 30 ,y= 30 ,area= 900 ,squared= 900
<init>DoubleSquare:x= 10 ,y= 5
DoubleSquare = 50 ,perimeter= 35
LongRectangle = 200
```
