ch = {}
for idx, s in enumerate(input()):
    if s in ch:
        ch[s].append(idx)
    else:
        ch[s] = [idx]

ch = sorted(ch.items())

N = len(ch)

dp = [[[0]*2 for _ in range(2)] for _ in range(N+1)]


for i in range(1, N+1):
    arr = ch[i-1][1]
    for j in range(2):
        if j == 1: arr.reverse()

        a =  dp[i-1][0][1] + abs(dp[i-1][0][0] - arr[0])
        b = dp[i-1][1][1] + abs(dp[i-1][1][0] - arr[0])

        flag = False
        if a < b:
            pos = dp[i-1][0][0]
            flag = True
        else:
            pos = dp[i-1][1][0]


        cnt = 0
        for c in arr:
            cnt += abs(c - pos)
            pos = c

        
        temp = dp[i-1][0][1] if flag else dp[i-1][1][1]

        dp[i][j][0] = pos
        dp[i][j][1] = temp + len(arr) + cnt
res = 2147000000
for d in dp[-1]:
    res = min(d[1], res)
print(res)
    
