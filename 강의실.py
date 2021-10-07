import sys
input = sys.stdin.readline
import heapq

N = int(input())
arr = []
for _ in range(N):
    i, s, e = map(int, input().split())
    arr.append([s, e])

arr.sort(key = lambda x : x[0])

H = []
res = 0


for s, e in arr:
    if H and s >= H[0]:
        heapq.heappop(H)  
    heapq.heappush(H, e)

    if res < len(H):
        res = len(H)
print(res)












""" 광고 삽입 방식
from collections import defaultdict
N = int(input())

dic = defaultdict(int)

for _ in range(N):
    b, s, e = map(int, input().split())
    dic[s] += 1
    dic[e] -= 1

dic = sorted(dic.items())
res = 0
for i in range(1, len(dic)):
    dic[i] = (dic[i][0], dic[i][1] + dic[i-1][1])

dic.sort(key = lambda x : x[1])
print(dic[-1][-1])
"""
