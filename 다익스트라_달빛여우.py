import sys
input = sys.stdin.readline
import heapq
Max = int(1e9) 


def D1():
    
    ch = [[0]*2 for _ in range(N+1)] #방문여부 체크
    dis = [[Max]*2 for _ in range(N+1)]
    H = [(0, 1, 0)]
    dis[1][1] = 0

    while H:
        v, now, who = heapq.heappop(H)
        if ch[now][who] == 1: continue
        ch[now][who] = 1
        for gv, gn in G[now]:
            mv = v + gv*4 if who else v+gv
            if  mv < dis[gn][who] :
                dis[gn][who] = mv
                heapq.heappush(H, (mv, gn, not(who)))
                
    return dis 


def D2():

    ch = [0]*(N+1)
    dis = [Max]*(N+1)
    H = [(0, 1)]
    dis[1] = 0
    
    while H:
        v, now = heapq.heappop(H)
        if ch[now] == 1: continue
        ch[now] = 1
        for gv, gn in G[now]:
            mv =  v+gv*2
            if mv  < dis[gn]:
                dis[gn] = mv
                heapq.heappush(H, (mv, gn))
    return dis
                
    



N, M = map(int, input().split())
G = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, d = map(int, input().split())
    G[a].append((d, b))
    G[b].append((d, a))


dis1 = D1()
dis2 = D2()

res =0 
for i in range(2, N+1):
    if dis2[i] < min(dis1[i]) :
        res += 1

print(res)



