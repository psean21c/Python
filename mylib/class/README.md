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


    
class CustomTopo():
  def __init__(self,address):
    print('CustomTopo')
    self.address = address  
  def update():
    print ("custom update")


cTopo1 = CustomTopo('Toronto')
print(cTopo1.address)

topo = Topo('Chicago')
print(topo.address + ",name=" + str(topo.name))


topo1 = Topo('New York','t1')
print(topo1.address + ",name=" + str(topo1.name))

```

Output
```
CustomTopo
Toronto
Topo
Chicago,name=None
Topo
New York,name=t1

```
