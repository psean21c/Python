'''
@author: Simon Park
version 1
'''
string = input()

lst_cmd = [i for i in input().split(" ")]
idx = int(lst_cmd[:1][0])
val = lst_cmd[1:][0]

string = string[:idx] + val + string[idx+1:]

print(string)

'''
version 2
'''
S=input()
i,c=map(str,input().split())
i=int(i)
print(S[:i] + c + S[i+1:])
