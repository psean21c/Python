
# @uwi
import sys
stdin = sys.stdin

n,m = map(int,stdin.readline().split())
rows = []
for i in range(n):
	rows.append(list(map(int,stdin.readline().split())))
col = int(stdin.readline())
for row in sorted(rows, key=lambda x:int(x[col])):
	print(' '.join(map(str,row)))


# @bradyz
i, k = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(i)]
n = int(input())
g.sort(key=lambda x: x[n])
for x in g:
    print(" ".join(map(str, x)))
