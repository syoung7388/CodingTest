



def Back(x, y):
    if x == 0 or y ==0 :return
    global res
    if s1[x-1] == s2[y-1]:
        res = s1[x-1]+res
        Back(x-1, y-1)
    else:
        if dp[x-1][y]>= dp[x][y-1]:
            Back(x-1, y)
        else:
            Back(x, y-1)
            

s1 = list(map(str, input()))
s2 = list(map(str, input()))
n1, n2 = len(s1), len(s2)
dp = [[0]*(n2+1) for _ in range(n1+1)]

for i in range(1, n1+1):
    for j in range(1, n2+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])


print(dp[-1][-1])


res = ""
Back(n1, n2)
print(res)

