def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
M = int(input())
gra = [list(map(int, input().split())) for _ in range(N)]
arr = list(map(int, input().split()))

parent = [x for x in range(N+1)]
for i in range(N):
    for j in range(N):
        if gra[i][j] == 0: continue
        if find(i+1) != find(j+1):
            union(i+1, j+1)

bf = parent[arr[0]]
res = "YES"
for a in arr:
    if bf != parent[a]:
        res = "NO"
        break
print(res)
