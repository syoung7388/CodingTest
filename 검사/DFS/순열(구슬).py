


def DFS(v):
    global cnt
    if v == M:
        for i in range(M):
            print(aws[i], end=" ")
        cnt += 1
        print()
        return
    else:
        for j in range(1, N+1):
            if ch[j] == 0:
                aws[v] = j
                ch[j] = 1
                DFS(v+1)
                ch[j]= 0
                
            
            


if __name__ == "__main__":

    N, M = map(int, input().split())
    aws = [0]*(N)
    ch = [0]*(N+1)
    cnt = 0
    DFS(0)
    print(cnt)
