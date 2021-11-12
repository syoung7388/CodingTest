import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())
Log = int(math.log2(N))+1
parent = [[0]*Log for _ in range(N+1)]
d = [0]*(N+1)
ch = [0]*(N+1)
G = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
   

def DFS(x, dep):
    ch[x] = True
    d[x] = dep
    for g in G[x]:
        if ch[g] == 1: continue
        parent[g][0] = x
        DFS(g, dep+1)
        
        
def set_parent():        
    DFS(1, 0)
    for i in range(1, Log):
        for j in range(1, N+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]
def LCA(a, b):
    if d[a] > d[b]:
        a, b = b, a
    for i in range(Log -1, -1, -1):
        if d[b] - d[a] >= (1<<i):
            b = parent[b][i]
    
    if a == b: return a
    
    for i in range(Log-1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    return parent[a][0]
set_parent()
M = int(input())
for i in range(M):
    a, b = map(int, input().split())
    print(LCA(a, b))
