import sys

def DFS(now):
    global rx, ry
    for g in G[now]:
        DFS(g)
        if rx == g:
            rx = now
        if ry == g:
            ry = now

    if rx == ry:
        print(T[rx][0], T[ry][1])
        sys.exit(0)




N = int(input())
arr = list(map(int, sys.stdin.readline().rstrip()))
rx, ry = map(int, input().split())
stack = []
T = {}
cnt = 1
G = [[] for _ in range(N+1)]
remove = []
for i in range(1, len(arr)+1):
    if arr[i-1] == 0:
        if rx == i or ry == i:
            remove.append(cnt)
        stack.append((cnt, i))
        cnt += 1
    elif arr[i-1] == 1:

        n, a = stack.pop()
        T[n] = [a, i]
        if rx == i or ry == i:
            remove.append(n)
        if not stack: continue
        G[stack[-1][0]].append(n)
rx, ry = remove
DFS(1)
