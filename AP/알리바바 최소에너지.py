N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dy = [[0]*N for _ in range(N)]
dy[0][0] = arr[0][0]

for i in range(N):
    dy[0][i] = dy[0][i-1]+arr[0][i] #(0,-1) => 0
    dy[i][0] = dy[i-1][0] + arr[i][0] #(-1,0) => 0
for i in range(1, N):
    for j in range(1, N):
        dy[i][j] = min(dy[i-1][j], dy[i][j-1])+arr[i][j]
    
print(dy[N-1][N-1])
