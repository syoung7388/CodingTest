

def DFS(x,y):

    gra[x][y] = 0
    for d in range(8):
        a = x + dx[d]
        b = y + dy[d]
        if 0 <= a < N and 0 <= b < N and gra[a][b] == 1:
            DFS(a,b)
    

if __name__ == "__main__":

    dx = [-1, -1,-1, 0,1,0,1,1]
    dy = [-1, 0, 1, 1,0,-1,1, -1 ]

    N = int(input())
    gra = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    res = [] 
    for i in range(N):
        for j in range(N):
            if gra[i][j] == 1:
                cnt += 1
                DFS(i,j)
 
    print(cnt)
                

    
