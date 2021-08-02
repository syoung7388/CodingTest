inf = 2147000000

N, K = map(int, input().split())

dy = [inf]*(K+1)
dy[0]=0
for _ in range(N):
    coin = int(input())
    for i in range(coin, K+1):
        dy[i] = min(dy[i-coin]+1, dy[i])

if dy[K] == inf:
    print(-1)
else:
    print(dy[K])
