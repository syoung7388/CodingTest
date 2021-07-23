



def DFS(L, last):
    global cnt

    if L == N:
        return
    if last == N-1:
        cnt += 1
        return
    else:
        for i in range(N): #0 ~ 4
            if ch[i] == 0 and gra[last][i]==1:
                ch[i] = 1
                DFS(L+1, i)
                ch[i]= 0






if __name__ == "__main__":
    N, M = map(int, input().split())

    gra = [[0]*N for _ in range(N)]

    for _ in range(M):
        x, y = map(int, input().split())
        gra[x-1][y-1] = 1

    ch = [0]*(N)
    cnt = 0
    ch[0] = 1

    DFS(0, 0)
    print(cnt)
        
        
