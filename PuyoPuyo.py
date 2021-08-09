import sys
input = sys.stdin.readline
def DFS(x, y):
    global cnt
    cnt += 1
    ch[x][y] = 1
    P[cnt]= (x,y)
    for k in range(4):
        xx = dx[k]+x
        yy = dy[k]+y
        if 0<=xx<6 and 0<=yy<12 and board[xx][yy]==board[x][y] and ch[xx][yy] == 0:
            DFS(xx, yy)




def change(arr):
    arr.sort(key= lambda x: x[1])
    for rx, ry in arr:
        board[rx].pop(ry)
        board[rx].insert(0, 0)




        
if __name__ == "__main__":
    gra = [list(map(str, input())) for _ in range(12)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    P = [[] for _ in range(72)]
    board = [[0]*12 for _ in range(6)]

    for a in range(12):
        for b in range(6):
            if gra[a][b] != '.':
                board[b][a] = gra[a][b]
    sc = 0
    cnt = 0
    temp = list()
    while True:
        ch=[[0]*12 for _ in range(6)]
        for i in range(6):
            for j in range(12):
                if board[i][j] != 0:
                    DFS(i, j)
                    if cnt >= 4:
                        for m in range(1, cnt+1):
                            temp.append((int(P[m][0]), int(P[m][1])))
                    cnt = 0
        if len(temp) > 0:
            sc+=1
            change(temp)
        else:
            break
        temp.clear()

        
    print(sc)
