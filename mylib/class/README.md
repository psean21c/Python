#


###

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
