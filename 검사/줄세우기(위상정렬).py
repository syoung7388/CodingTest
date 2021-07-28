from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

ch = [0]*N
G = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    ch[b-1] += 1
    G[a-1].append(b)
    
Q = deque()

for i in range(N):
    if ch[i] == 0:
        Q.append(i)

res = ""
while Q:
    q = Q.popleft()
    res += str(q+1)+" "
    for j in G[q]:
        ch[j-1]-=1
        if ch[j-1] == 0:
            Q.append(j-1)
print(res)
