from collections import deque
def DFS(V):
    global res
    res += str(V+1)+ " "
    for i in range(N):
        if G[V][i] == 1 and ch[i] == 0:
            ch[i] = 1
            DFS(i)
if __name__ == "__main__":
    N, M, V = map(int, input().split())
    G = [[0]*N for _ in range(N)]
    for _ in range(M):
        x, y = map(int, input().split())
        G[x-1][y-1] =1
        G[y-1][x-1] =1

    ch = [0]*N
    ch[V-1] = 1
    res = ""
    DFS(V-1)
    print(res)

    ch = [0]*N
    ch[V-1] = 1
    res =""
    H = deque()
    H.append(V-1)
    while H:
        h = H.popleft()
        res += str(h+1)+" "
        for j in range(N):
            if G[h][j] == 1 and ch[j] == 0:
                ch[j] = 1
                H.append(j)
       

    print(res)
