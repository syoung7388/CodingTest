def getStr(w, h):
    if w == 0 and h == 0: return 1
    if dp[w][h] != -1: return dp[w][h]
    dp[w][h] = 0
    if w > 0:
        dp[w][h] += getStr(w-1, h+1)
    if h > 0:
        dp[w][h] += getStr(w, h-1)
    return dp[w][h]
    
    
    
    
while True:
    N = int(input())
    if N == 0:
        break
        
    dp = [[-1]*((N*2)+1) for _ in range(N+1)]
    
    
    print(getStr(N, 0)) #전체, 반알
