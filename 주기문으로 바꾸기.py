N = int(input())
dic = {6:7, 7:8, 8:10, 9:12, 10:14, 11:16}
if N< 6:
    print(N)
elif N <= 7:
    print(dic[N])
elif N<12:
    print(N + N%6)
else:
    dp = [0]*(N+1)
    for k, v in dic.items():
        dp[k] = v
    for i in range(12, N+1):
        dp[i] = i+dp[i-6]
    print(dp[N])
