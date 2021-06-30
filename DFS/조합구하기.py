# 1~N ... M개를 뽑는


def DFS(v, s):
    global cnt
    if v == M:
        for j in p:
            print(j, end=" ")
        cnt += 1
        print()
        return
    else:
        for i in range(s, N+1):
            p[v] = i
            DFS(v+1, i+1)

if __name__ == "__main__":
    N, M = map(int, input().split())
    p = [0]*(M)
    cnt= 0 

    DFS(0, 1)
    print(cnt)
