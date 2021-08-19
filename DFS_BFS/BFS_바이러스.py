from collections import deque


N = int(input())
M = int(input())
gra = [[] for _ in range(N)]
for _ in range(M):
    n1, n2 = map(int, input().split())
    gra[n1-1].append(n2-1)
    gra[n2-1].append(n1-1)
ch = [0]*N
ch[0] = 1
Q =deque()
Q.append(0)

while Q:
    now = Q.popleft()
    for next in gra[now]:
        if ch[next] == 0:
            Q.append(next)
            ch[next] = 1

print(ch.count(1)-1)


