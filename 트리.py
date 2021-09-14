
def DFS(x):
    global res
    if not G[x]:
        res += 1
        return

    for nt in G[x]:
        DFS(nt)

N = int(input())
nums = list(map(int, input().split()))

G = [[] for _ in range(N)]
delete = int(input())


for i in range(N):
    if nums[i] == -1:
        root = i
        continue
    if i == delete:
        continue

    G[nums[i]].append(i)

res = 0
if root != delete:
    DFS(root)
print(res)
