# 1st
N = int(input())
num = ""
for i in range(N):
    num += str(i+1)
    
print (num)
    
# 2nd
N = int(input())
for i in range(1, N+1):
    print(i, end="")

# 3rd
N = int(input())
print(*range(1,N+1), sep='')

# 4th
print("".join(map(str,list(range(1,int(input())+1)))))
