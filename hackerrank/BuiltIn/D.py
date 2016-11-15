'''

12
insert 0 5
insert 1 10
insert 0 6
print 
remove 6
append 9
append 1
sort 
print
pop
reverse
print
----------------
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
'''
# 1)
N = int(input())
#print(N)
lst = []
lst_command = []

for i in range(N):
    q = str(input())
    lst_command = q.split(' ')
    if lst_command[0] == 'insert':
        idx = int(lst_command[1])
        val = int(lst_command[2])
        lst.insert(idx,val)
    elif lst_command[0] == 'append':
        val = int(lst_command[1])
        lst.append(val)
    elif lst_command[0] == 'remove':
        val = int(lst_command[1])
        lst.remove(val)
    elif lst_command[0] == 'pop':
        lst.pop()
    elif lst_command[0] == 'sort':
        lst.sort()
    elif lst_command[0] == 'reverse':
        lst.reverse()
    elif lst_command[0] == 'print':
        print(lst)


        import sys

# 2)
if __name__ == '__main__':
    N = int(sys.stdin.readline())
    A = []
    
    for _ in range(N):
        X = sys.stdin.readline().strip().split()
        
        if X[0] == 'print':
            print(A)
        else:
            f, args = X[0], list(map(int, X[1:]))
            getattr(A, f)(*args)
            
