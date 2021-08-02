
import sys
def DFS(x, y):
    ch[x][y] = 1
    if x == 0:
        print(y)
        sys.exit(0)
    else:
        if y+1 < 10 and ch[x][y+1] == 0 and gra[x][y+1] == 1:
            DFS(x, y+1)
        elif 0 <= y-1 and ch[x][y-1] == 0 and gra[x][y-1] == 1:
            DFS(x, y-1)
        else:
            DFS(x-1, y)
            
        


if __name__ == "__main__":

    gra = [list(map(int, input().split())) for _ in range(10)]
    ch = [[0]*(10) for _ in range(10)]

    for c in range(10):
        if gra[9][c] == 2:
            DFS(9, c)
    
