from collections import deque




dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
ch = set()

def Move(T1, T2, gra):
    
    temp = []
    
    #위, 아래, 왼, 오 이동
    for k in range(4):
        x1, y1, x2, y2 = T1[0]+dx[k], T1[1]+dy[k], T2[0]+dx[k], T2[1]+dy[k] 
        if gra[x1][y1] == 1 or gra[x2][y2] == 1: continue
        if ((x1, y1), (x2, y2)) not in ch:
            temp.append(((x1, y1), (x2, y2)))
            ch.add(((x1, y1), (x2, y2)))
    
    
    #회전
    
    #가로
    if T1[0] == T2[0]:
        
        #d = -1 일때
        if gra[T1[0]-1][T1[1]] == 0 and gra[T2[0]-1][T2[1]] == 0: 
            
            minus =  (T1, (T1[0]-1, T1[1]))
            if minus not in ch:
                temp.append(minus)
                ch.add(minus)
            minus =  (T2, (T2[0]-1, T2[1]))
            if minus not in ch:
                temp.append(minus)
                ch.add(minus)
           
        #d = +1 일때
        elif gra[T1[0]+1][T1[1]] == 0 and gra[T2[0]+1][T2[1]] == 0:
            
            plus =  (T1, (T1[0]+1, T1[1]))
            if  plus not in ch:
                temp.append(plus)
                ch.add(plus)
                
            plus = (T2, (T2[0]+1, T2[1]))
            if plus not in ch:
                temp.append(plus)
                ch.add(plus)    
        
    
    #세로
    else:
        if gra[T1[0]][T1[1]-1] == 0 and gra[T2[0]][T2[1]-1] == 0:
            minus = ((T1[0], T1[1]-1), T1)
            if minus not in ch:
                temp.append(minus)
                ch.add(minus)
                
            minus =  ((T2[0], T2[1]-1), T2)
            if minus not in ch:
                temp.append(minus)
                ch.add(minus)
                
        elif gra[T1[0]][T1[1]+1] == 0 and gra[T2[0]][T2[1]+1] == 0:
            
            plus =  ((T1[0], T1[1]+1),T1)
            if plus not in ch:
                temp.append(plus)
                ch.add(plus)
                
            plus =  ((T2[0], T2[1]+1),T2)
            if plus not in ch:
                temp.append(plus)
                ch.add(plus)
    return temp
        
    



def solution(board):
        N = len(board)
        ch.add(((1, 1), (1, 2)))
        Q = deque([((1, 1), (1, 2),0)])
        
        gra = [[1 for _ in range(N+2)]]    
        for b in board:
            b = [1]+b+[1]
            gra.append(b)
        gra.append([1]*(N+2))
        
        
        while Q:
            T1, T2, cnt = Q.popleft()
            if T1 == (N, N) or T2 == (N, N):
                return cnt
    
            nQ = Move(T1, T2, gra)
            for q in nQ:
                Q.append((q[0], q[1], cnt+1))
