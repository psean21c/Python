'''
@author: simon.park
version 1
'''

N=int(input())
# 1) Put all inputs to list of students 
students = []
for i in range(N):
    students.append([x for x in input().strip().split()])

# 2) convert grades from string to floating 
report = []
for x in students:
    report.append([x[0],float(x[1]),float(x[2]),float(x[3])])

# 3) Find out the grades of the student
name = str(input())
grades = []
for x in report:
    if x[0] == name:
        grades = [x[1],x[2],x[3]]

print("%.2f" %(sum(grades) /3))



'''
version 2
'''
n = int(input())
dic = {}
for _ in range(n):
    line = [i for i in input().strip().split(' ')]
    grades = list(map(float, line[1:]))

    dic[line[0]] = sum(grades)/len(grades)

name = str(input())
print('{0:.2f}'.format(dic[name]))
