from collections import deque

if __name__ == "__main__":
    N, M = map(int, input().split())
    gra = [list(map(str, input())) for _ in range(N)]
    dis = [[0]*M for _ in range(N)]
    Q = deque()
    for i in range(N):
        for j in range(M):
            if gra[i][j] == 'S':
                Q.appendleft((i,j))
            if gra[i][j] == 'D':
                end = (i, j)
            if gra[i][j] == '*':
                Q.append((i, j))


    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    flag = False
    while Q:
        if flag:
            break
        x, y = Q.popleft()
        for k in range(4):
            xx, yy = x+dx[k], y+dy[k]
            if not (0<=xx<N and 0<=yy<M):
                continue
            #물
            if gra[x][y] == '*':
                if gra[xx][yy] == '.' or gra[xx][yy]=='S':
                    Q.append((xx, yy))
                    gra[xx][yy] = '*'
            #고슴도치
            elif gra[x][y] == 'S':
                if gra[xx][yy] == '.':
                    gra[xx][yy] = 'S'
                    dis[xx][yy] = dis[x][y]+1
                    Q.append((xx, yy))
                if gra[xx][yy] == 'D':
                    flag = True
                    dis[xx][yy] = dis[x][y] + 1
                    break
if dis[end[0]][end[1]]== 0:
    print('KAKTUS')
else:
    print(dis[end[0]][end[1]])
    
