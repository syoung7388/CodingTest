
def DFS(L, s):
    global res
    if L == 10:
        res = max(res, s)
        return
    for i in range(4):
        if arrive[i] == 1: continue
        
        cur = pos[i]
        if len(r[cur]) == 2:
            n = z[L]-1
            cur = r[cur][1]
        else:
            n = z[L]
        
        for _ in range(n):
            cur = r[cur][0]
            if cur == 32: 
                arrive[i] = 1
                break


        if cur == 32 or ch[cur] == 0:
            
            ch[cur] = 1
            b = pos[i]
            pos[i] = cur
            ch[b] = 0

            DFS(L+1, s+v[cur])


            ch[cur] = 0
            arrive[i] = 0
            pos[i] = b
            ch[b] = 1

            
r = {0:[1], 1:[2], 2:[3], 3:[4], 4:[5], 5:[6, 21], 6:[7], 7:[8], 8:[9],9:[10], 10:[11, 30], 11:[12], 12:[13],13:[14], 14:[15], 15:[16, 27], 16:[17], 17:[18], 18:[19], 19:[20], 20:[32], 21:[22], 22:[23], 23:[24], 24:[25], 25:[26], 26:[20], 27:[28], 28:[29], 29: [24], 30:[31], 31:[24]}

v= [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 13, 16, 19, 25, 30, 35, 28, 27, 26, 22, 24, 0]

N = len(v)
ch = [0]*(N+1)
pos = [0]*4
arrive = [0]*(4)
arr = [[] for _ in range(4)]
val = [[] for _ in range(4)]
z = list(map(int, input().split()))
res = 0
DFS(0, 0)
print(res)
