N,M = map(int, input().split())
nl = list(map(int, input().split()))

s= e = 0
cnt = 0
while True:
    add = sum(nl[s:e+1])
    if add < M:
        e += 1
    elif add == M:
        s += 1
        cnt += 1
    else:
        s += 1
    if e == N:
        break

print(cnt)
