from collections import deque

ch = set()
dx, dy = [-1,0, 1, 0], [0, 1, 0, -1]

def Move(T1, T2, cnt, gra):
    Q = []
    #4격자 탐색
    for k in range(4):
        x1, y1, x2, y2 = dx[k]+T1[0], dy[k]+T1[1], dx[k]+T2[0], dy[k]+T2[1]
        if gra[x1][y1] == 0 and gra[x2][y2] == 0 and not ((x1, y1), (x2, y2)) in ch:
            ch.add(((x1, y1), (x2, y2)))
            Q.append(((x1, y1), (x2, y2), cnt+1))
    
    if T1[0] == T2[0]: 
        for d in [-1, 1]:
            if gra[T1[0]+d][T1[1]] == 0 and gra[T2[0]+d][T2[1]] == 0:
                nt = ((T1[0]+d, T1[1]), T1)
                if not nt  in ch:
                    ch.add(nt)
                    Q.append((nt[0], nt[1], cnt+1))
                nt = ((T2[0]+d, T2[1]), T2)
                if nt not in ch:
                    ch.add(nt)
                    Q.append((nt[0], nt[1], cnt+1))
    else:
        for d in [-1, 1]:
            if gra[T1[0]][T1[1]+d]==0 and gra[T2[0]][T2[1]+d] == 0:
                nt = (T1 ,(T1[0], T1[1]+d))
                if not nt in ch:
                    ch.add(nt)
                    Q.append((nt[0], nt[1], cnt+1))                
                nt = (T2, (T2[0], T2[1]+d))
                if nt not in ch:
                    ch.add(nt)
                    Q.append((nt[0], nt[1], cnt+1))    
    return Q
 
def solution(board):
    N = len(board)
    gra = [[1]*(N+2) for _ in range(N+2)]
    for i in range(N):
        for j in range(N):
            gra[i+1][j+1] = board[i][j]
            
    NQ = deque()
            
    ch.add(((1, 1), (1, 2)))
    NQ.append(((1, 1), (1, 2), 0))
    while NQ:
        pos1, pos2, cnt = NQ.popleft()
        if pos1 == (N, N) or pos2 == (N, N):
            return cnt
        
        nq = Move(pos1, pos2, cnt, gra)
        for q in nq:
            NQ.append(q)
            
