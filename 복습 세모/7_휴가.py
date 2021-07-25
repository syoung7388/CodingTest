




def DFS(L, pay):
    global bf
    if L == N+1:
        if pay > bf:
            bf = pay
    else:
        if L+T[L] <= N+1:
            DFS(L+T[L], pay+P[L])
        DFS(L+1, pay)


 
if __name__ == "__main__":
    N= int(input())
    T = [0] # 일자
    P = [0] #주는 돈
    for n in range(N):
        t,p = map(int, input().split())
        T.append(t)
        P.append(p)
    bf = -2147000000
    DFS(1, 0)
    print(bf)
