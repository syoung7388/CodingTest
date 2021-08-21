s1 = list(map(str, input()))
s2 = list(map(str, input()))
n1, n2 = len(s1), len(s2)
dy = [['']*(n2+1) for _ in range(n1+1)]
for i in range(1, n1+1):
    for j in range(1, n2+1):
        if s1[i-1] == s2[j-1]:
            dy[i][j] = dy[i-1][j-1] + s1[i-1]
        else:
            dy[i][j] = dy[i-1][j] if len(dy[i-1][j]) > len(dy[i][j-1]) else dy[i][j-1]

print(len(dy[-1][-1]))
print(dy[-1][-1])

