



def DFS(v): 
    if v == M:
        global cnt
        cnt += 1
        for j in range(M):
            print(res[j], end =" ")
        print()
        
    else:
        for i in range(1, N+1): #1~3
            res[v] = i
            DFS(v+1)
            



if __name__ == "__main__":
    N,M = map(int, input().split())#구슬 수  #M번을 뽑음
    res = [0]*M
    cnt = 0
    DFS(0)
    print(cnt)


