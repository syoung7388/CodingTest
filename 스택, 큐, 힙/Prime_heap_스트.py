import heapq
N, E = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(E):
    x, y, v = map(int, input().split())
    G[x-1].append((v, y-1))
    G[y-1].appned((v, x-1))
    
ch = [0]*N
H = []
H.append((0,0))
cnt = 0
res = 0
while cnt < N:
    v1, dot1 = heapq.heappop(H)
    if ch[dot1] == 0:
        res += v1
        cnt += 1
        ch[dot1] = 1
        for v2, dot2 in G[dot1]:
            if ch[dot2] == 0:
                heapq.heappush(H,(v2, dot2))
print(res)
