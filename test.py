from collections import deque


def solution(bro):
    N = len(bro)
    gra=  [[-1]*(N+2) for _ in range(N+2)]
    for i in range(N):
        for j in range(N):
            gra[i+1][j+1] = bro[i][j]
    ch = set([((1, 1), (1, 2))])
    
    Q = deque([([1, 1], [1, 2], 0)])
    dx, dy =[-1, 0, 1, 0], [0, 1, 0, -1]
    
    while Q:
        pos1, pos2, cnt = Q.popleft()
        if pos1 == (N, N) or pos2 == (N,N):
            return cnt
        
        #평행 이동
        for k in range(4):
            x1, y1, x2, y2 = pos1[0]+dx[k], pos1[1]+dy[k], pos2[0]+dx[k], pos2[1]+dy[k]
            npos1 = (x1, y1)
            npos2 = (x2, y2)
            if gra[x1][y1]==1 or gra[x2][y2] == 1: continue
            if (npos1, npos2) not in ch:
                Q.append((npos1,npos2, cnt+1))
                ch.add((npos1, npos2))
        
        #회전
        if pos1[0] == pos2[0]: #가로방향
            for d in [-1, 1]:
                if gra[pos1[0]+d][pos1[1]] == 1 or gra[pos2[0]+d][pos2[1]] == 1: continue #사각형이 all 0
                
                if (npos1, (npos1[0]+d, npos1[1])) not in ch:
                    Q.append((npos1, (npos1[0]+d, npos1[1]), cnt+1))
                    ch.add((npos1, (npos1[0]+d, npos1[1])))
                    
                if (npos2, (npos2[0]+d, npos2[1])) not in ch:
                    Q.append((npos2, (npos2[0], npos2[1]), cnt+1))
                    ch.add((npos2, (npos2[0]+d, npos2[1])))
        else:
            for d in [-1, 1]:     
                
                if gra[pos1[0]][pos1[1]+d] == 1 or gra[pos2[0]][pos2[1]+d] == 1: continue #사각형이 all 0
                
                
                if ((npos1[0], npos1[1]+d), npos1) not in ch:
                    Q.append(((npos1[0], npos1[1]+d), npos1, cnt+1))
                    ch.add(((npos1[0], npos1[1]+d), npos1))
                if ((npos2[0], npos2[1]+d), npos2) not in ch:
                    Q.append(((npos2[0], npos2[1]+d), npos2, cnt+1))
                    ch.add(((npos2[0], npos2[1]+d), npos2))
                    
                    
                
 

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))
