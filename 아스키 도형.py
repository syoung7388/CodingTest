
N, M = map(int, input().split())
gra = [[ord(x) for x in input()] for _ in range(N)]

res = 0



for i in range(N):
    flag = False
    s = 0
    for j in range(M):
        if gra[i][j] == 47 or gra[i][j] == 92:
            flag = not(flag)
            s += 1
        if flag and gra[i][j] == 46:
            res += 1
    res += s // 2
print(res)
            
            
        
