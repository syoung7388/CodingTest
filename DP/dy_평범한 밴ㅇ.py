N, K = map(int, input().split())
dy = [0]*(K+1)
for _ in range(N):
    w, v= map(int, input().split())
    for i in range(K, w-1, -1):
        dy[i] = max(dy[i-w]+v, dy[i])

print(dy[K])
