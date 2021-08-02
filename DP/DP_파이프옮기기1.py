def Move(x, y, d):
    for dir in direction[d]:
        xx = x+cos[dir][0]
        yy = y+cos[dir][1]
        if 0<=xx<N and 0<=yy<N and gra[xx][yy] ==0:
            if dir !=2:
                dy[xx][yy][dir] += dy[x][y][d]
            else:
                if gra[xx-1][yy] == 0 and gra[xx][yy-1] == 0:
                    #45도씩 회전 #꼭 빈 칸이어야 하는 곳은 색으로 표시되어져 있다.
                    dy[xx][yy][dir] += dy[x][y][d] 
if __name__ == "__main__":
    N = int(input())
    gra = [list(map(int, input().split())) for _ in range(N)]
    dy = [[[0]*3 for _ in range(N)] for _ in range(N)]
    dy[0][1][0] = 1
    direction = {0:[0,2], 1:[1,2], 2:[0,1,2]}
    cos = [[0,1], [1,0], [1,1]]
    
    
    for x in range(N):
        for y in range(N):
            for d in range(3):
                if gra[x][y] == 0 and dy[x][y][d] != 0:
                    Move(x, y, d)
    print(sum(dy[N-1][N-1]))
                    
