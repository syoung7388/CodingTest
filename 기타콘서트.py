def DFS(L, bit, cnt):
    global res
    if L == N:
        if (1<<M+1)-1 == bit:
            res = min(cnt, res)
        return

    DFS(L+1, bit|gita[L], cnt+1)
    DFS(L+1, bit, cnt)



N, M = map(int, input().split())
gita = []
for _ in range(N):
    name, pos = map(str, input().split())   
    bit = 1<<(M)
    for p in range(M):
        if pos[p] == 'Y':
            bit |= (1<<p)
    gita.append(bit)





#함수에 들어가야할거 ? L, bit, cnt


res = 2147000000
DFS(0, 1<<M , 0)
print(res)




#print(bin((1<<M+1) -1))


    



