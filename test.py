

S = input()
dic = dict()

N = len(S)
for i in range(N):
    if S[i] in dic:
        dic[S[i]].append(i)
    else:
        dic[S[i]] = [i]
M = len(dic)
dic = sorted(dic.items())
dp = [[[0]*2 for _ in range(2)] for _ in range(M+1)]

for i in range(1, M+1):
    arr = dic[i-1][1]

    for j in range(2):
        if j == 1: arr.reverse()

        r0 = dp[i-1][0][1] + abs(dp[i-1][0][0] - arr[0])
        r1 = dp[i-1][1][1] + abs(dp[i-1][1][0] - arr[0])
        flag = True
        if r0 < r1:
            pos = dp[i-1][0][0]
        else:
            flag = False
            pos = dp[i-1][1][0]
            
        dis = 0
        for a in arr:
            dis += abs(a - pos)
            pos = a
        
        
        if flag:
            cnt =  dp[i-1][0][1] 
        else:
            cnt =  dp[i-1][1][1]
        
        
        dp[i][j][0] = pos
        dp[i][j][1] = cnt+dis+len(arr)

        
print(min(dp[-1][0][1], dp[-1][1][1]))
