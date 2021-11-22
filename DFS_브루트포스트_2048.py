import sys
input = sys.stdin.readline

def getmax(g):
    result = 0
    for i in g:
        result = max(max(i), result)
    return result
    
def Left(G):
    result = []
    for i in range(N):
        arr = []
        ch = []
        for j in range(N):
            if G[i][j] == 0: continue
            if arr and arr[-1] == G[i][j] and ch[-1] == 0:
                arr[-1] += G[i][j]
                ch[-1] = 1
            else:
                arr.append(G[i][j])
                ch.append(0)
        arr  += [0]*(N-len(arr))
        result.append(arr)
    return result

def Right(G):
    result = []
    for i in range(N):
        arr = []
        ch = []
        for j in range(N-1, -1, -1):
            if G[i][j] == 0: continue
            if arr and arr[-1] == G[i][j] and ch[-1] == 0:
                arr[-1] += G[i][j]
                ch[-1] = 1
            else:
                arr.append(G[i][j])
                ch.append(0)
        arr  += [0]*(N-len(arr))
        arr.reverse()
        result.append(arr)
    return result
def Up(G):
    result = Left(list(map(list, zip(*G))))
    return list(map(list, zip(*result)))


def Down(G):
    result = Right(list(map(list, zip(*G))))
    return list(map(list, zip(*result)))
 
def DFS(L, g):
    global res
    if L == 5:
        res = max(res, getmax(g))
        return


    DFS(L+1, Left(g))
    DFS(L+1, Right(g))
    DFS(L+1, Up(g))
    DFS(L+1, Down(g))
    
    


N = int(input())
gra = [list(map(int, input().split())) for _ in range(N)]

res = 0
DFS(0, gra)
print(res)
