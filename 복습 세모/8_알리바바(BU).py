
#알리바바와 40인의 도둑




N = int(input())
gra= [list(map(int, input().split())) for _ in range(N)]
dy = [[0]*N for _ in range(N)]
dy[0][0] = gra[0][0]
for i in range(1,N):
    dy[0][i] = dy[0][i-1]+gra[0][i]
    dy[i][0] = dy[i-1][0]+gra[i][0]


for a in range(1, N):
    for b in range(1 , N):
        dy[a][b] = min(dy[a-1][b], dy[a][b-1])+gra[a][b]
print(dy[N-1][N-1])
    
