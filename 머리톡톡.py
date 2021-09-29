import sys
from collections import defaultdict

N = int(input())

if N == 1:
    print(0)
    exit()
arr = defaultdict(int)
ans = defaultdict(int)
    
l = [0]*N

for i in range(N):
    a = int(input())
    arr[a] += 1
    l[i] = a

for i, v in arr.items():
    ans[i] += v-1
    for j in range(2*i, 1_000_001, i):
        if  j in arr:
            ans[j] += v
print(ans)
for i in l:
    print(ans[i])

