N = int(input()) #회원수

div = [[55]*(N+1) for _ in range(N+1)]
hh = [0]*(N)

while True:
    f1 , f2 = map(int, input().split())
    if f1 == -1 and f2 == -1:
        break
    div[f1][f2] = 1
    div[f2][f1] = 1

for s in range(1, N+1):
    div[s][s] = 0


for k in range(1, N+1):
    for i in range(1, N+1):
        bf = 0
        for j in range(1, N+1):
                div[i][j] = min(div[i][k] + div[k][j], div[i][j])
                if div[i][j] > bf:
                    bf = div[i][j]
        hh[i-1] = bf



mi = min(hh)
print(mi,hh.count(mi))


for c in range(len(hh)):
    if mi == hh[c]:
        print(c+1)
        
