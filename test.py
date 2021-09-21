
def DFS(now):
    global cnt
    if not G[now]:
        cnt += 1
        return
    for next in G[now]:
        DFS(next)

N = int(input())
nodes = list(map(int, input().split()))
delete = int(input())

G = [[] for _ in range(N)]

for i in range(N):
    if nodes[i] == -1:
        root = i
        continue
    if i == delete: 
        continue
    G[nodes[i]].append(i)
cnt = 0
if root != delete:
    DFS(root)
print(cnt)
