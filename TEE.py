"""
빠_늑대: x//2 -> x
여우 : x -> x*2
느_늑대: x*2 -> x*4
"""

import heapq
import sys
input = sys.stdin.readline

def fox():
    ch = [0]*(N+1)
    H = [(0, 1)]
    
    while H:
        d, now = heapq.heappop(H)
        if ch[now] == 1: continue
        ch[now] = 1
        for gd, gn in G[now]:
            nd = gd*2 + d
            if nd < dis_f[gn]:
                dis_f[gn] = nd
                heapq.heappush(H, (nd, gn))
  

def wolf():
    ch = [[0]*2 for _ in range(N+1)]
    H = [(0, 1, 0)]
    while H:
        d, now, f = heapq.heappop(H)
        if ch[now][f] == 1: continue
        ch[now][f] = 1
        for gd, gn in G[now]:
            if f == 0:
                nd = gd + d
            else:
                nd = gd*4 + d
            nf = not(f)
            if nd < dis_w[gn][nf]:
                dis_w[gn][nf] = nd
                heapq.heappush(H, (nd, gn, not(f)))
    
N, M = map(int, input().split())
G = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, v = map(int,input().split())
    G[a].append((v, b))
    [b].append((v, a))

Max = 214700000
dis_f = [Max]*(N+1)
dis_f[1] = 0
fox()

dis_w = [[Max]*2 for _ in range(N+1)]
dis_w[1][0] = 0
wolf()

print(dis_f)
print(dis_w)

res= 0 
for i in range(2, N+1):
    if dis_f[i] < min(dis_w[i]):
        res += 1
print(res)

