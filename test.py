

def find(x):
    if parent[x] == x:
        return x
    return find(parent[x])


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
        dic[a] += dic[b]
    else:
        parent[a] = b
        dic[b] += dic[a]


N = int(input())
M = int(input())
parent = [x for x in range(N+1)]
dic = {}
for _ in range(M):
    a, b = map(int, input().split())
    if a not in dic:
        dic[a] = 1
    if b not in dic:
        dic[b] = 1
    if find(a) != find(b):
        union(a, b)

print(dic[1]-1)
