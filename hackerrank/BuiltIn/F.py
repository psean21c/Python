N=int(input())
listA = list(map(int, input().split()))[:N]
max_value = max(listA)
while max_value == max(listA):
    listA.remove(max(listA))
max_next = max(listA)
print (max_next)
