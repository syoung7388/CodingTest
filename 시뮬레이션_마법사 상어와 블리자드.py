"""
list로 만들기
1) 블리자드(마법)
   - 8씩 증가하면서 구슬 파괴
   - pull진행
2) 폭발 
  - 4개 이상인거 찾기 while 문 안에 while문
3) 변화 
  - stack을 이용해서 진행한다 
"""

import sys
input = sys.stdin.readline
dx, dy = [0, 0, 1, 0, -1], [0, -1, 0, 1, 0]
change = [0, 4, 2, 1, 3]
def make_list():
    x, y = N//2, N//2
    g_list = [gra[x][y]]
    L , d, flag = 1, 1, 1
    while flag:
        for i in range(4):
            if not flag: break
            for _ in range(L):
                xx, yy = dx[d]+x, dy[d]+y
                g_list.append(gra[xx][yy])
                if xx == 0 and yy == 0:
                    flag = False
                    break
                x, y = xx, yy
            if i == 1:
                L += 1
            d += 1
            if d == 5:
                d = 1
        L += 1  
    return g_list    
        
def magic(st, s):
    pos = 0
    for _ in range(s):
        pos += st
        g[pos] = 0
        st += 8
        
    ng = [0]
    for i in range(1, N):
        if g[i] == 0: continue
        ng.append(g[i])
    ng += [0]*(N - len(ng))
    return ng

def explosion():
    global g, res
    while True:
        flag = True
        idx = 1
        while idx < N-4:
            if g[idx] != 0 and g[idx] == g[idx+1] and g[idx+1] == g[idx+2] and g[idx+2] == g[idx+3]:   
                n, cnt, flag = g[idx], 0, False
                for j in range(idx, N):
                    if g[j-cnt] == n:
                        g.pop(j-cnt)
                        cnt += 1
                    else:
                        idx = j - cnt
                        break
                res += n*cnt
                g += [0]*cnt
            else:
                idx += 1
        if flag: break                
                        
def transform():
    ng = []
    for i in range(1, N):
        if g[i] == 0: break
        if ng and g[i] == ng[-1]:
            ng[-2] += 1
        else:
            ng.append(1)
            ng.append(g[i])
    ng = [0]+ng
    ng += [0]*(N-len(ng))
    return ng
            
            
        
        
        
#main
N, M = map(int, input().split())
gra = [list(map(int, input().split())) for _ in range(N)]
g = make_list()
res = 0
N = N*N
for _ in range(M):
    d, s = map(int, input().split())
    d = change[d]
    g = magic(d*2-1, s)
    explosion()
    g = transform()
print(res)
    
