from collections import deque
def Move(p1, p2, gra):
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    temp = []
    for k in range(4):
        x1, y1,x2, y2 = dx[k]+p1[0], dy[k]+p1[1], dx[k]+p2[0], dy[k]+p2[1]
        if gra[x1][y1] == 1 or gra[x2][y2] == 1: continue
        temp.append(((x1, y1), (x2, y2)))
        
    if p1[0] == p2[0]: #가로
        for d in [-1, 1]:
            if gra[p1[0]+d][p1[1]] == 1 or gra[p2[0]+d][p2[1]] == 1: continue
            
            temp.append(((p1[0]+d, p1[1]), p1))
            temp.append(((p2[0]+d, p2[1]), p2))
        
    else:#세로
        for d in [-1, 1]:
            if gra[p1][p1[1]+d] == 1 or gra[p2][p2[1]+d] == 1: continue
            temp.append((p1, (p1[0], p1[1]+d)))
            temp.append((p2, (p2[0], p2[1]+d)))
    return temp    




def solution(board):
    N = len(board)
    gra = [[1]*(N+2) for _ in range(N+2)]
    
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                gra[i+1][j+1] = 0
    
    Q =  deque([((1, 1), (1, 2), 0)])
    
    ch = set()
    ch.add(((1, 1), (1, 2)))
    
    
    while Q:
        p1, p2, cnt = Q.popleft()
        
        if p1 == (N, N) or p2 == (N, N):
            print(cnt)
            break
        
        
        for t in Move(p1, p2, gra):
            if not t in ch:
                nt = cnt+1
                Q.append((t[0], t[1], nt))
                ch.add(t)

