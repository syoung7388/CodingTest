
import sys
input = sys.stdin.readline

N, D = map(int, input().split())
arr = [[] for _ in range(10001)]

for _ in range(N):
    s, e, d = map(int, input().split())
    arr[s].append([d, e])
dis = [x for x in range(D+1)] 
for i in range(D+1):

    #지름길 안가고 갈때
    if i != 0:

        dis[i] = min(dis[i], dis[i-1]+1)

    #지름길 중에 선택
    for d, e in arr[i]:
        if e <= D and dis[e] > d+dis[i]:
            dis[e] = d+dis[i]


print(dis[D])







"""

import heapq
N, D = map(int, input().split())
dic = {}


for _ in range(N):
    s, e, d = map(int, input().split())
    if s in dic:
        dic[s].append((e, d))
    else:
        dic[s] = [(e, d)]

dic[D] = []
key = sorted(dic.keys())


H = []
heapq.heappush(H, (0,0))

while H:
    d, now = heapq.heappop(H)
    if now == D:
        print(d)
        break
    #지름길로 이동
    if now in key:
        for ed, dis in dic[now]:
            heapq.heappush(H, (d+dis, ed))
            
    #그냥 쌩으로 고속도로 타기
    for k in key:
        if k > now:
            heapq.heappush(H, (d+(k-now), k))
            break
   
"""
