def DFS(x, y, ch, total):
    global res
    if len(ch) == N+1:
        res += total
        return
    for k in range(4):
        xx, yy = x+dx[k], y+dy[k]
        if (xx, yy) not in ch:
            ch.append((xx, yy))
            DFS(xx, yy, ch, total*pro[k]*0.01)
            ch.pop()


dx, dy = [-1,1, 0, 0], [0, 0, -1, 1]


N, D, S, M, B = map(int, input().split())
pro = [D, S, M, B]

res = 0
DFS(0, 0, [(0, 0)], 1)
print(res)
