import sys
input = sys.stdin.readline
N, C = map(int, input().split())

box = [tuple(map(int, input().split())) for _ in range(int(input()))]
box.sort(key = lambda x:x[1])
arr = [0]*(N+1)
res =0
#O(M)+O(MlogM)
for s, e, cnt in box:

    m = max(arr[s:e])
    if C == m: continue
    if C - m >= cnt:
        load = cnt
    else:
        load = C-m

    for i in range(s, e):
        arr[i] += load
    res += load
print(res)
    
