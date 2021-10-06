def DFS(now, v):
    global res
    ch[now] = 1
    if now == e-1:
        res = v
        return 
    for nv, nt in G[now]:
        if ch[nt] == 0:
            DFS(nt, v+nv)
    return

N, M = map(int, input().split())

G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b, v = map(int, input().split())
    G[a-1].append((v, b-1))
    G[b-1].append((v, a-1))

for _ in range(M):
    s, e = map(int, input().split())
    ch = [0]*(N)
    res = 0
    DFS(s-1, 0)
    print(res)
