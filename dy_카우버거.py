import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
dy = [[-1]*(K+1) for _ in range(M+1)]

dy[M][K] = 0
res = 0

for _ in range(N):
    a, b = map(int, input().split())
    for i in range(M+1):
        for j in range(K+1):
            if dy[i][j] != -1 and i-a >= 0 and j-b>=0:
                dy[i-a][j-b] = max(dy[i-a][j-b], dy[i][j]+1)
                res = max(res, dy[i-a][j-b])
    for d in dy:
        print(d)
    print()
