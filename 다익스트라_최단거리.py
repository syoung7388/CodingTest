import heapq


N, M = map(int, input().split())
st = int(input())

G = [[] for _ in range(N)]
for i in range(M):
    a, b, v = map(int, input().split())
    G[a-1].append((v, b-1))
    
    
H = []
heapq.heappush(H, (0, st-1))

Max = 2147000000
res = [Max]*(N)
res[st-1] = 0

ch = [0]*N

while H:
    v, now = heapq.heappop(H)
    if ch[now] == 1: continue
    ch[now] = 1
    for gv, gn in G[now]:
        if ch[gn] != 0 or v + gv < res[gn]: continue
        res[gn] = v+gv
        heapq.heappush(H, (v+gv, gn))
       
    
    
        
        
for r in res:
    if r == Max:
        print("INF")
    else:
        print(r)
