def DFS(L, sum):
    global cnt
    if sum > T:
        return
    if L == k:     
        if sum == T:
            cnt+=1
            return
    else:
        for i in range(N[L]+1):
            DFS(L+1, sum+(i*C[L]))
                

if __name__ == "__main__":
    T = int(input())
    k = int(input())
    C = list()
    N = list()
    cnt = 0
 
    
    for _ in range(k):
        c,n = map(int, input().split())
        C.append(c)
        N.append(n)

    DFS(0, 0)
    print(cnt)
