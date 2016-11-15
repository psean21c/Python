# version 1
N=int(input())
students = []
lowest = 100
for i in range(N):
    lst = []
    x = input() 
    y = float(input())
    lowest = min(lowest,y)
    lst.append(x)
    lst.append(y)
    students.append(lst)




listA = [[name,mark] for name, mark in students if mark > lowest]


lowest = 100
for lst in listA:
    if lst[1] < lowest:
        lowest = lst[1]

listA.sort()
for lst in listA:
    if lst[1] == lowest:
        print(lst[0])


# version 2

N=int(input())
students = []
lowest = 100
for i in range(N):
    x = input() 
    y = float(input())
    students.append([x,y])
    lowest = min(lowest,y)


#print(students)

listA = [[name,mark] for name, mark in students if mark > lowest]
#print(listA)

secondLowest = min([lst[1] for lst in listA])
#print(secondLowest)

listB = [listA[0] for listA in listA if listA[1] ==secondLowest]
listB.sort()
for lst in listB:
    print(lst)
