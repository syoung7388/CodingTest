import sys
input = sys.stdin.readline

dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
def union(pos):
    n_ball = []
    for k, v in pos.items():
        x, y = k
        m, s, d, cnt, cd = v
        if cnt  ==1:
            n_ball.append([x, y, m, s, cd])
        else:
            n_m = m//5
            if n_m == 0: continue
            n_s = s//cnt
            if d == 0 or d == cnt: temp = [0, 2, 4, 6]
            else: temp = [1, 3, 5, 7]
            for i in temp:
                n_ball.append([x, y, n_m, n_s, i])
         
    return n_ball            


N, M, K = map(int, input().split())
ball = [list(map(int, input().split())) for _ in range(M)]

for _ in range(K):
    
    pos = {}
    
    #볼 이동
    for x, y, m, s, d in ball:
        a, b = s*dx[d] , s*dy[d]

        xx, yy = (x+a)%N, (y+b)%N
        if (xx, yy) not in pos:
            pos[(xx, yy)]= [m, s, d%2, 1, d] #마지막 카운트
        else:
            pos[(xx,yy)][0] += m
            pos[(xx,yy)][1] += s
            pos[(xx,yy)][2] += d%2
            pos[(xx,yy)][3] += 1
    
   
    ball = union(pos)
res = 0
for x, y, m, s, d in ball:
    res += m
print(res)
