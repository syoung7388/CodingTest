from collections import defaultdict


N, K = map(int, input().split())
arr = list(map(int, input().split()))

S = sum(arr)
bf = arr[0]
num =  S - K
dica = defaultdict(int)
dicb = defaultdict(int)
cnt = 0
for i in range(1, N):

    nb= S-bf
    if num - nb in dica:
        cnt += dica[num-nb]

    dica[bf] += 1
    dicb[nb] += 1
    bf = bf+arr[i]

res = cnt + dica[K] + dicb[K]
if S == K:
    res += 1
print(res)

