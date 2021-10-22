N, M = map(int, input().split())
row = [list(map(int, input())) for _ in range(N)]


bc = 0
gc = 0
for a in range(N):
    s = 0
    for b in range(M):
        s += row[a][b]
    if s %2 != 0:
        bc += 1
    else:
        gc += 1


br = 0
bc = 0
for b in range(M):
    s = 0
    for a in range(N):
        s += row[b][a]
    if s % 2 != 0:
        br += 1
    else:
        gc += 1
if br%2 == 0:
    res = br +bc
    if N +M - res < res:
        res = N+M-res
else:
    res = br + gc
    if N+M-res < res:
        res = N+M-res
print(res)
        
