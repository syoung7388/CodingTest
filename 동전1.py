N, K = map(int, input().split())
dy = [0]*(K+1)
dy[0] = 1

for _ in range(N):
    coin = int(input())
    for i in range(coin,K+1):
        dy[i] = dy[i]+dy[i-coin]
print(dy)
print(dy[K])
