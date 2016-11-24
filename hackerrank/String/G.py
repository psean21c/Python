
# 1) 
def printList(s):
  for i in s:
    print(i.capitalize() + " ", end="")

s = input().split()
printList(s)

# 2)
s = input()
for x in s[:].split():
    s = s.replace(x, x.capitalize())
print(s)

