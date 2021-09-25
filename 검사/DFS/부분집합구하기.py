 #집합의 부분집합 출력


def DFS(n):
    if n == N+1:
        for i in range(1, N+1):
            if ch[i] == 1:
                print(i, end=" ")
        print()
    else:   
        ch[n] = 1
        DFS(n+1)
        ch[n] = 0
        DFS(n+1)
        


if __name__ == "__main__":
    N = int(input())
    ch = [0]*(N+1)
    DFS(1)
    
