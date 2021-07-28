#우선수위큐 & 다익스트라
import sys
import heapq 


inf = 21476000000

n = int(input())
m = int(input())
bus= [[] for _ in range(n)]

for _ in range(m):
    a, b, w = map(int, input().split())
    bus[a-1].append((b-1, w)) #도착지점, 돈

print(bus)

s,e  = map(int, input().split())
H = []
heapq.heappush(H, (0, s-1))
check= [inf for _ in range(n)]
check[s-1] = 0


while H:
    count, city = heapq.heappop(H) #쌓인돈 // 시작도시
    print("카운트, 시티", count, city)
    if city == e-1:
        break
    for c, cnt in bus[city]: #도착도시// 돈
        if count + cnt < check[c]:
            check[c] = count+cnt
            heapq.heappush(H, (count+cnt, c))
    print(H)
print(check[b-1])
        
    
        


    



