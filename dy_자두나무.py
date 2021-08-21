
A, M = map(int, input().split())

dy = [[[-1]*(M+1) for _ in range(3)] for _ in range(A+1)]
dy[0][1][0] = 0
app = [int(input()) for _ in range(A)]
app.insert(0, 0)
for i in range(A): #떨어지는 사과
    for j in range(1, 3): # 사과나무
        for k in range(M):
            if dy[i][j][k] == -1: continue
            #이동 안하기
            if app[i+1] == j:
                dy[i+1][j][k] = max(dy[i][j][k]+1, dy[i+1][j][k])
            else:
                dy[i+1][j][k] = max(dy[i][j][k], dy[i+1][j][k])

            #이동 하기

            if k+1 > M: continue
            if j == 1:
                if j+1 == app[i+1]:
                    dy[i+1][j+1][k+1] = max(dy[i][j][k]+1, dy[i+1][j+1][k+1])
                else:
                    dy[i+1][j+1][k+1] = max(dy[i][j][k], dy[i+1][j+1][k+1])
            else:
                if j-1 == app[i+1]:
                    dy[i+1][j-1][k+1] = max(dy[i][j][k]+1, dy[i+1][j-1][k+1])
                else:
                    dy[i+1][j-1][k+1] = max(dy[i][j][k], dy[i+1][j-1][k+1])
for d in dy:
    print(d)
