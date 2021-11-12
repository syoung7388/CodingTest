import sys
def ABC(cnt, a, b, s):
    if len(s) == N:
        if cnt  == K:
            print(s)
            sys.exit(0)
        return
    if dp[cnt][a][b] != -1:
        return
    dp[cnt][a][b] = 1
    
    ABC(cnt, a+1, b, s+"A")
    ABC(cnt+a, a, b+1, s+"B")
    ABC(cnt+a+b, a, b, s+"C")
    return
    
N, K = map(int, input().split())

dp = [[[-1]*(N+1) for _ in range(N+1)] for _ in range(N*(N-1)//2+1)]

ABC(0, 0, 0, "")
print(-1)
