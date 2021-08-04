from collections import deque
if __name__ == "__main__":
    S = int(input())
    Q = deque()
    Q.append((1, 0))
    ch = [[-1]*(S+1) for _ in range(S+1)]
    ch[1][0] = 0
    
    while Q:
        x, y = Q.popleft()
        if ch[x][x] == -1: #저장
            ch[x][x] = ch[x][y]+1
            Q.append((x,x))
        if x+y <= S and ch[x+y][y] == -1:
            ch[x+y][y] = ch[x][y]+1
            Q.append((x+y,y))
        if x-1 >= 0 and ch[x-1][y] == -1:
            ch[x-1][y] = ch[x][y]+1
            Q.append((x-1, y))

            
r = ch[S][1]
for i in range(1, S):
    if ch[S][i] != -1:
        r = min(r, ch[S][i])
print(r)
