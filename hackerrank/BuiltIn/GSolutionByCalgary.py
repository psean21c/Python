# -*- coding: utf-8 -*-

# 
is_simulation_mode = False
#is_simulation_mode = True

#---------------------------------------


def p(obj, *therest):
    if is_simulation_mode:
        print(obj, *therest)
    return

input_data_text = \
'''
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
'''

import collections 
input_q = collections.deque()
input_data = input_data_text.split('\n')
for i in input_data:
    if i == '':
        input_data.remove(i)
for i in input_data:    
    input_q.appendleft(i) 
# 
def input_from_both():  
    if is_simulation_mode:
        return input_q.pop()        
    else:       
        return input()

## data e.g.------------------
#--------------------------------     
#main
p('Start!!')

input_t = input_from_both()

students = []
for _ in range(int(input_t)):
    students.append([input_from_both(), float(input_from_both())])
        
def getKey(item):
    return item[1]

students = sorted(students, key=getKey)
p(students)

name_list   = []

is_2nd_score_set = False
the_score = students[0][1]

for s in students:
    if is_2nd_score_set == False and s[1] > the_score:
        the_score = s[1] 
        is_2nd_score_set = True
    if is_2nd_score_set == True and s[1] == the_score:
        name_list.append(s[0])        
p(name_list)
name_list.sort()
for n in name_list:
    print(n)
p('End!!')

# build first and prepare excel /chrom
