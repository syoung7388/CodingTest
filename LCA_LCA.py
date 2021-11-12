import sys
sys.setrecursionlimit(10**6)

def DFS(x, dep):
    ch[x] = 1
    d[x] = dep
    for y in G[x]:
        if ch[y] == 1: continue
        parent[y] = x
        DFS(y, dep+1)


def LCA(a, b):

    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]

    while a != b:
        a = parent[a]
        b = parent[b]
    return a


N = int(input())
parent = [0]*(N+1)
d = [0]*(N+1)
ch = [0]*(N+1)

G = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

DFS(1, 0)

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(LCA(a, b))
