
N, a, b = map(int, input().split())
dy = [x for x in range(N+1)]

for i in (a, b):
    for j in range(i+1, N+1):
        dy[j] = min(dy[j-i-1]+1, dy[j])

print(dy[N])
