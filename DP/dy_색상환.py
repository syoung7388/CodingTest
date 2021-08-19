N= int(input()) #색의 개수
K = int(input()) #K개 선택
dy = [[0]*(N+1) for _ in range(K+1)]
dy[1] = [x for x in range(N+1)]
for i in range(2, K+1):
    for j in range(i*2, N+1):
        dy[i][j] = dy[i-1][j-2]+dy[i][j-1]


print(dy[K][N])
