



def DFS(L,P):
    global cnt
    if L == N:
        cnt += 1
        for j in range(P):
            print(chr(p[j]+64), end='')
        print()
        return
    else:
        for i in range(1, 27):
            if code[L] == i:
                p[P] = i
                DFS(L+1, P+1)
            elif i >= 10 and code[L] == i//10 and code[L+1] == i%10:
                p[P] = i
                DFS(L+2, P+1)

if __name__ == "__main__":
    code = list(map(int, input()))
    N = len(code)
    code.insert(N,-1)
    p = [0]*(N+3)
    cnt = 0
    DFS(0,0)
    print(cnt)
