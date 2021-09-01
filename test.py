#20개 - 1000m
#이동 가능 happy 불가 "sad"

#1. 좌표사이에서 이동가능 한지 안한지 체크
#2. 이동가능 한지 확인 0~n+1까지

import sys
sys.setrecursionlimit(10**6)

def check(pos):
    ch = [[] for _ in range(M+2)]
    for i in range(M+2):
        for j in range(M+2):
            if i == j: continue
            dis = abs(pos[i][0]-pos[j][0])+abs(pos[i][1]-pos[j][1])
            if dis <= 1000:
                ch[i].append(j)
    return ch

def DFS(x):
    vis[x] = 1
    for next in ch[x]:
        if vis[next] == 0:
            DFS(next)
    return
for _ in range(int(input())):
    M = int(input())
    pos = [list(map(int, input().split())) for _ in range(M+2)]
    ch = check(pos)
    vis = [0]*(M+2)
    DFS(0)
    if vis[M+1] == 0:
        print("sad")
    else:
        print("happy")
