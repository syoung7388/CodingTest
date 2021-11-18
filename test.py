import heapq
import sys
input = sys.stdin.readline
def wolf():
    H = [(0, 1, False)] #val, 현재위치, flag
    ch = [0]*(N+1)
    while H:
        v, now, flag = heapq.heappop(H)
        if ch[now][flag] == 1: continue    
        ch[now][flag] = 1
        
        for gv, gn in G[now]:
            if flag:
                mv = v+gv
            else:
                mv = v+gv*4
            if mv < dis_w[gn]:
                dis_w[gn] = mv
                heapq.heappush(H, (mv, ng, not(flag)))
    
Max = 2147000000
N, M = map(int, input().split())
G = [[] for _ in range(N+1)]

for _ in range(N):
    a, b, d = map(int, input().split())
    G[a].append((d, b))
    G[b].append((d, a))

dis_w = [[Max]*2 for _ in range(N+1)]
dis_w[1][1] = 0
wolf()
dis_f = [Max]*(N+1)
fox()
dis_f[1] = 0
    
