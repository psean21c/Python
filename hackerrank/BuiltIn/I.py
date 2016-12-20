
from operator import itemgetter


X =[int(a) for a in input().strip().split()]
N,M = X

  
lst = []
for _ in range(N):
    l = [int(a) for a in input().strip().split()]
    lst.append(l)


idx = int(input())

lst2 = sorted(lst, key=itemgetter(idx))

for ls in lst2:
    for l in ls:
        print(l,end=' ') 
    print()
