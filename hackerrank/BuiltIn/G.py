'''
@author: simon.park
version 1
'''

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

# It will creat another list which remove the students having the lowest grade    
listA = [[name,mark] for name, mark in students if mark > lowest]

# This is the worst part because it runs another loop - O(N) - to find out the next(2nd) lowest grade
lowest = 100
for lst in listA:
    if lst[1] < lowest:
        lowest = lst[1]

listA.sort()
for lst in listA:
    if lst[1] == lowest:
        print(lst[0])


'''
@author: simon.park
version 2
'''

# Simplify the way to make the students list
N=int(input())
students = []
lowest = 100
for i in range(N):
    x = input() 
    y = float(input())
    students.append([x,y])
    lowest = min(lowest,y)

#print(students)

# The same as the version-1
listA = [[name,mark] for name, mark in students if mark > lowest]
#print(listA)

# Get the next lowest grade which will be used for next step
secondLowest = min([lst[1] for lst in listA])
#print(secondLowest)

# Get the list of names which has the another lowest grade
listB = [listA[0] for listA in listA if listA[1] ==secondLowest]
listB.sort()

# Print names
for lst in listB:
    print(lst)
