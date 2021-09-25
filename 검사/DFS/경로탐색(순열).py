def DFS(last):
    global cnt
    if last == N:
        cnt+= 1
        """
        for a in range(1, N+1):
            if p[a] == 1:
                print(a, end=" ")

        """
        return
    else:
        for i in range(1,N+1):
            if p[i] == 0 and gra[last][i] == 1:
                p[i] = 1
                DFS(i)
                p[i]=0
                

if __name__ == "__main__":
    N, M = map(int, input().split())
    gra = [[0]*(N+1) for _ in range(N+1)]
    p = [0]*(N+1)
    p[1] = 1
    cnt = 0
    for i in range(M):
        a1, a2 = map(int, input().split())
        gra[a1][a2] = 1
    DFS(1)
    print(cnt)
   
    

