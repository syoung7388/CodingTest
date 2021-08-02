#동전 교환


N= int(input())
coins = list(map(int, input().split()))
remain = int(input())

dy = [550]*(remain+1)
dy[0] = 0
for c in coins:
    for i in range(c, remain+1):
        dy[i] = min(dy[i-c]+1, dy[i])
print(dy[remain]) 
