from collections import deque
import sys

def BFS(x, y):
    Q = deque([(x, y)])
    dis[x][y] = 0
    while Q:
        x, y = Q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            while True:
                if not (0<=nx<N and 0<=ny<M): break
                if gra[nx][ny] == '*': break
                if  dis[x][y]+1 > dis[nx][ny]: break

                Q.append((nx, ny))
                dis[nx][ny] = dis[x][y]+1
                nx = nx+dx[i]
                ny = ny+dy[i]


if __name__ == "__main__":
    M, N = map(int, input().split())

    gra = [input() for _ in range(N)]
    dx, dy = (0, 1,0, -1), (1, 0, -1, 0)

    C = []

    for i in range(N):
        for j in range(M):
            if gra[i][j] == 'C':
                C.append((i, j))
    (sx, sy), (ex, ey) = C

    dis = [[float('inf')]*M for _ in range(N)]
    BFS(sx, sy)

    print(dis[ex][ey]-1)
