N = int(input())

dy = [[0]*(10) for _ in range(N)]
dy[0] = [1 for _ in range(10)]
dy[0][0] = 0


for i in range(1, N):
    for j in range(10):
        if j+1 > 9:
            dy[i][j] = dy[i-1][j-1]
        elif j-1 <0:
            dy[i][j] = dy[i-1][j+1]
        else:
            dy[i][j] = dy[i-1][j-1]+dy[i-1][j+1]
       

print(sum(dy[N-1]))
