import sys

ch = [[] for _ in range(26)]

arr = set()
for idx, s in enumerate(sys.stdin.readline().rstrip()):
    ch[ord(s) - 97].append(idx)
    arr.add(ord(s) - 97)
    
arr = sorted(arr)
N = len(arr)


dp = [[[0]*2 for _ in range(2)] for _ in range(N+1)]


for i in range(1, N+1):
    for j in range(2):
        if j == 1: ch[arr[i-1]].reverse()

        n = dp[i-1][0][1] + abs(dp[i-1][0][0] - ch[arr[i-1]][0])
        y = dp[i-1][1][1] + abs(dp[i-1][1][0] - ch[arr[i-1]][0])

        flag = False
        
        if n<y:
            pos = dp[i-1][0][0]
            flag = True
        else:
            pos = dp[i-1][1][0]

            
        cnt = 0
        for c in ch[arr[i-1]]:
            cnt += abs(c-pos)
            pos = c

        temp =  dp[i-1][0][1]if flag else dp[i-1][1][1]
     
        dp[i][j][0] = pos
        dp[i][j][1] = temp + cnt + len(ch[arr[i-1]])
       


res = 2147000000
for d in dp[-1]:
    res = min(res, d[1])
print(res)
