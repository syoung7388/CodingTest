def Send(w, h):
    if dp[w][h] != -1: return dp[w][h]
    dp[w][h] = 0
    if w == 0 and h == 0: return 1
    
   
    if w > 0:
        dp[w][h] += Send(w-1, h+1)
    if h > 0:
        dp[w][h] += Send(w, h-1)
    return dp[w][h]
 

dp = [[-1]*(31) for _ in range(61)]
while True:
    N = int(input())
    if N == 0:
        break
    print(Send(N, 0))
