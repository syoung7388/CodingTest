

from heapq import heappush, heappop
import sys
input = sys.stdin.readline



N, E = map(int, input().split()) #정점의 개수
G = [[] for _ in range(N)]


for _ in range(E):
    x, y, v = map(int, input().split())
    G[x-1].append((v, y-1))
    G[y-1].append((v, x-1))


Q = []
Q.append((0, 1))

res = 0
cnt = 0
ch = [0]*N
while cnt < N:
    value, dot1 = heappop(Q)
    if ch[dot1] == 0:        
        res += value
        cnt += 1
        ch[dot1] =1
        for v, dot2 in G[dot1]:
            if ch[dot2] == 0:
                heappush(Q, (v, dot2))
        
        
    
print(res)
    
    
