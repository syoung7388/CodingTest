N = int(input())

pos =[list(map(int, input().split())) for _ in range(N)]
pos.sort(key = lambda x: -x[0])

p_len = 0
for i in range(N):
    r = False
    l = False
    for j in range(i+1, N):
        if pos[i][0] == pos[j][0]: continue
        if not r and pos[j][1]< pos[i][2] <= pos[j][2]:
            r = True
            p_len += pos[i][0] - pos[j][0]  
        if not l and pos[j][1]<= pos[i][1] < pos[j][2]:
            l = True
            p_len += pos[i][0] - pos[j][0]
    if not r:
        p_len += pos[i][0]
    if not l:
        p_len += pos[i][0]
print(p_len)
