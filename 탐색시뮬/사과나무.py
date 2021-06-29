
N = int(input())
nl = [list(map(int, input().split())) for _ in range(N)]

go = N // 2
n = e = go

add = 0
for i in range(N): #0~4
    for j in range(n,e+1):
        add += nl[i][j]
    if i < go:
        n -= 1
        e += 1
    else:
        n += 1
        e -= 1
print(add)
