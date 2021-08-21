import sys
sys.setrecursionlimit(10**6)
def getHim(x, y):
    if x == y:
        return 1
    elif x == 0:
        return 2
    elif abs(x-y)%2 == 0:
        return 4
    else:
        return 3
def solve(n, l, r):
    if n >= len(order)-1:
        return 0

    if dy[n][l][r] != -1:
        return dy[n][l][r]
    dy[n][l][r] = min(solve(n+1, order[n], r)+getHim(l, order[n]),
                         solve(n+1, l, order[n])+getHim(r, order[n]))
    return dy[n][l][r]
    
order = list(map(int, input().split()))
dy = [[[-1]*5 for _ in range(5)] for _ in range(len(order))]

print(solve(0,0,0))
