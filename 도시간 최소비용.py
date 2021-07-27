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



s,e  = map(int, input().split())
que = []
heapq.heappush(que, (0, s-1))
check= [inf for _ in range(n)]
check[s-1] = 0



while que:
    count, city = heapq.heappop(que)
    if cuty == e-1:
        break
    for c, cnt in bus[city]:
        if count + cnt < check[c]:
            check[c] = count+cnt
            heapq.heappush(que, (count+cnt, c))
print(check[b-1])
        
    
        


    



