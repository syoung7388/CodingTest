import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
chx = defaultdict(int)
chy = defaultdict(int)
arr = []
for i in range(N):
    x, y = map(int, input().split())
    chx[x] += 1
    chy[y] += 1
    arr.append((x, y))

res = 0

for ax, ay in arr:
    res += (chx[ax]-1)*(chy[ay]-1)
    
print(res)
