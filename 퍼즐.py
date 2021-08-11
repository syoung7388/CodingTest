import sys
from collections import deque
if __name__ == "__main__":
    gra = [list(map(int, input().split())) for _ in range(3)]
    move = [1, 3, -1, -3]
    res = 2147000000
    Q = deque()
    S = ""
    res = "123456780"
    
    for i in range(3):
        for j in range(3):
            S += str(gra[i][j])
            if gra[i][j] == 0:
                temp = i*3 + j
    Q.append((temp, S, 0))
    ch = set([S])


    while Q:
        now, s, cnt = Q.popleft()
        if s == "123456780":
            print(cnt)
            sys.exit(0)
        for k in move:
            next = now+k
            if not(0<=next<9): continue
            tem = list(s)
            tem[now], tem[next] = tem[next], tem[now]
            tem = ''.join(tem)
            if tem in ch: continue
            ch.add(tem)
            Q.append((next, tem, cnt+1))
    print(-1)
