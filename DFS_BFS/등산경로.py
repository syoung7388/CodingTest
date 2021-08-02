

import sys


def DFS(x, y):
    global cnt
    if x == ma_i[0] and y == ma_i[1]:
        cnt+=1
        return
    else:
        for i in range(4):
            a = x+dx[i]
            b = y+dy[i]
            if 0 <= a <=N-1 and 0 <= b <=N-1:
                if gra[x][y] < gra[a][b]:
                    DFS(a,b)

if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    cnt = 0
    N = int(input())
    gra = list()
    mi = 2147000000
    ma = -2147000000
    mi_i = (0,0)
    ma_i = (0,0)

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    for n in range(N):
        nums = list(map(int, input().split()))
        gra.append(nums)
        if min(nums) < mi:
            mi = min(nums)
            mi_i = (n, nums.index(mi))
        if max(nums) > ma:
            ma = max(nums)
            ma_i = (n, nums.index(ma))
    DFS(mi_i[0], mi_i[1])
    print(cnt)

