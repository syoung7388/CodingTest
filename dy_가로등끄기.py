import math
def getWatt(l, r, flag):
    if dp[l][r][flag] != -1:
        return dp[l][r][flag]
    if flag:
        cur = lamp[r][0] #M = 오른쪽
    else:
        cur = lamp[l][0] #M = 왼쪽
    print(cur)
    left = right = math.inf
    on = light[N-1]-light[r]+light[l-1]
    if l > 0:
        left = getWatt(l-1, r, 0)+ (cur-lamp[l-1][0])*on
    if r < N-1:
        right =  getWatt(l, r+1, 1)+ (lamp[r+1][0]-cur)*on

    dp[l][r][flag] = min(left, right)
    
    return dp[l][r][flag]

    


#main
N, M = map(int, input().split())
M-= 1
lamp = []
light = [0]
for _ in range(N):
    a,b = map(int, input().split())
    lamp.append((a, b))
    light.append(light[-1]+b)
light.pop(0)
print(light)
print(lamp)

dp = [[[-1]*2 for _ in range(N)] for _ in range(N)]
dp[0][N-1][0] = dp[0][N-1][1] = 0

print(getWatt(M, M, 0))
        


