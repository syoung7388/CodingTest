import heapq

left = []
right = []

N, M = map(int, input().split())



for i in list(map(int, input().split())):
    if i < 0:
        heapq.heappush(left, i)
    else:
        heapq.heappush(right, -i)



a, b = 0, 0
if right: a = -right[0]
if left: b = -left[0]

Max = max(a, b)



res = 0

while left:
    res+= -heapq.heappop(left)*2
    for _ in range(M-1):
        if not left : break
        heapq.heappop(left)
while right:
    res+= -heapq.heappop(right)*2
    for _ in range(M-1):
        if not right : break
        heapq.heappop(right)    


print(res-Max)

"""

from collections import deque
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
Q = deque(arr)

res = []

while Q:
    if abs(Q[0]) > abs(Q[-1]):
        a = Q.popleft()
        res.append(abs(a))
        for _ in range(M-1):
            if not Q : break
            if (a > 0 and Q[0]>0) or (a <0 and Q[0] < 0):
                Q.popleft()
    else:
        a = Q.pop()
        res.append(abs(a))
        for _ in range(M-1):
            if not Q : break
            if (a > 0 and Q[-1]>0) or (a <0 and Q[-1] < 0):
                Q.pop()
anw = 0
anw += res[0]

for i in range(1, len(res)):
    anw += res[i]*2
print(anw)
"""
