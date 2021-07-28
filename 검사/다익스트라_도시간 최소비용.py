import heapq
inf = 2147000000
N = int(input())
M = int(input())
Spot = [[] for _ in range(N)]
for _ in range(M):
    x, y, v = map(int, input().split())
    Spot[x-1].append((y-1, v))
S, E = map(int, input().split())
H = []
heapq.heappush(H, (0, S-1))
check = [inf for _ in range(N)]
check[S-1] = 0


while H:
    money, s_city = heapq.heappop(H)
    if s_city == E-1:
        break
    for e_city, plusmoney in Spot[s_city]:
        addmoney = money+plusmoney
        if addmoney < check[e_city]:
            check[e_city] = addmoney
            heapq.heappush(H, (addmoney, e_city))
print(check[E-1])
