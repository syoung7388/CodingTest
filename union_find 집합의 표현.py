import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(x):
    if head[x] < 0:
        return x
    head[x] = find(head[x])
    return head[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b: return
    if a < b:
        head[a] += head[b]
        head[b] = a
    else:
        head[b] += head[a]
        head[a] = b
        
        
        
N, M = map(int, input().split())
head = [-1]*(N+1)
for _ in range(M):
    cmd, a, b= map(int, input().split())
    if not cmd:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")

