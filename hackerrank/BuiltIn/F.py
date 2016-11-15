N=int(input())
lst = list(map(int, input().split()))[:N]
max_value = max(lst)
while max_value == max(lst):
    lst.remove(max(lst))
max_next = max(lst)
print (max_next)
