from itertools import combinations, permutations


def D(c):
    global res
    for per in permutations(c, N):
        dis = 0
        for idx, p in enumerate(per):
            dis += abs(Z[idx][0] - p[0]) + abs(Z[idx][1] - p[1])
        res = min(res, dis)
        




def DFS(x, y, n):
    global cnt
    cnt += 1
    ch[n]=1
    for k in range(4):
        xx, yy = dx[k]+x, dy[k]+y
        if (xx, yy) in com and ch[com.index((xx, yy))] == 0:
            DFS(xx, yy, com.index((xx, yy)))
        

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

gra = [list(map(str, input())) for _ in range(5)]
Z = []
arr = []
for i in range(5):
    for j in range(5):
        if gra[i][j] == '*':
            Z.append((i, j))
        arr.append((i, j))


N = len(Z) #조각수
res = 2147000000
for com in combinations(arr, N):
    cnt = 0
    ch = [0]*(N)
    DFS(com[0][0], com[0][1], 0)
    if cnt != N: continue
    D(com)

print(res)
