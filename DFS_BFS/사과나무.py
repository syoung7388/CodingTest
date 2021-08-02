from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]
N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
ch = [[0]*N for _ in range(N)]
sum = 0
Q =deque()
lo = N//2

ch[lo][lo] = 1
sum += a[lo][lo]
Q.append((lo, lo))
L=0

while True:
    if L == lo:
        break
    size = len(Q)
    for i in range(size):
        tmp = Q.popleft()
        for j in range(4):
            x = tmp[0]+dx[j]
            y = tmp[1]+dy[j]
            if ch[x][y] == 0:
                sum += a[x][y]
                ch[x][y] =1
                Q.append((x,y))
    L+=1
print(sum)
