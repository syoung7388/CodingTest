


def DFS(x, y):
    global num
    num += 1
    gra[x][y] = 0

    for i in range(4):
        a = x+ dx[i]
        b = y+dy[i]
        if 0 <= a <= N-1 and 0 <= b <= N-1 and gra[a][b] == 1:
            DFS(a, b)


if __name__ == "__main__":

    N = int(input())
    gra = [list(map(int, input())) for _ in range(N)]
    dx = [-1,0,1,0]
    dy= [0,-1,0,1]
    num = 0
    aws = []
 
    for i in range(N):
        for j in range(N):
            if gra[i][j] == 1:
                num = 0
                DFS(i, j)
                aws.append(num)

    print(len(aws)) 
    for w in sorted(aws):
        print(w)
    
