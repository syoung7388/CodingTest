


#순열구하기 1~N



def DFS(L):
    global cnt

    if L == M:
        for j in range(M):
            print(res[j], end=" ")
        cnt += 1
        print()
        return

    for i in range(N):
        if ch[i] == 0:
            res[L] = i+1
            ch[i] = 1
            DFS(L+1)
            ch[i]=0
        
    


if __name__ == "__main__":

    N, M = map(int, input().split())
    ch = [0]*N
    res = [0]*M
    cnt = 0

    DFS(0)
    print(cnt)
