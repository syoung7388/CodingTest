import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

#main
N = int(input()) #도로개수
W = int(input()) #사건개수
pos = [(1, 1), (N, N)]
for _ in range(W):
    pos.append(tuple(map(int, input().split())))
dp = [[-1]*(W+2) for _ in range(W+2)] #사건개수 + 경찰차2


def Move(x, y):
    if x > W or y > W: return 0
    if dp[x][y] != -1: return dp[x][y]
    
    pick = max(x, y)+1
    
    #1번 경찰차가 수행
    one = Move(pick, y)+abs(pos[x][0]-pos[pick][0])+abs(pos[x][1]-pos[pick][1])
    
    #2번 경찰차가 수행
    two = Move(x, pick)+abs(pos[y][0]-pos[pick][0])+abs(pos[y][1]-pos[pick][1])
    
    dp[x][y] = min(one, two)
    return dp[x][y]



def Back(x, y):
    if x > W or y > W: return
    pick = max(x, y)+1
    one = abs(pos[x][0]-pos[pick][0])+abs(pos[x][1]-pos[pick][1])
    two = abs(pos[y][0]-pos[pick][0])+abs(pos[y][1]-pos[pick][1])
    
    if dp[pick][y]+one < dp[x][pick]+two:
        print(1)
        Back(pick, y)
    else:
        print(2)
        Back(x, pick)
    return
    

#res 
print(Move(0,1))
Back(0,1)
