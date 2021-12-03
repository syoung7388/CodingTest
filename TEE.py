
def DFS(L, s):
    global res
    if L == 10:
        res = max(res, s)
        return


    
    for i in range(1, 5):
        if ch[i] == 1: continue
        x, y = pos[i]
        arrive = y+z[L]
        if arrive >= arr[x]:
            ch[i] = 1
            nx, ny = 0, 0
        elif x == 0 and route[x][arrive] %10 == 0 and route[x][arrive] != 40:
            nx, ny = route[x][arrive]//10, 0
        else:
            nx, ny = x, arrive

        if (nx, ny) in pos.items(): continue

        pos[i] = (nx, ny)
        DFS(L+1, s+route[nx][ny])
        ch[i] = 0
        pos[i] = (x, y)

        


route = [[0]+[x*2 for x in range(1, 21)], [10,13, 16, 19, 25, 30, 35, 40],[20, 22, 24, 25, 30, 35, 40], [30,28, 27, 26, 25, 30, 35, 40]]
arr = [21,8,7,8]




pos = {1:(0, 0), 2:(0, 0), 3:(0, 0), 4:(0, 0)}
ch = [0]*(5)
z = list(map(int, input().split()))
res = 0

DFS(0, 0)
print(res)
