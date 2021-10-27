

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
"""

def DFS(L, s):
    global res
    if L == 2:
        S = arr[P[1]] - arr[P[0]-1]
        print(P, S)
        if S == K:
            res += 1
        
        return 
    for i in range(s, N):
        P[L] = i
        DFS(L+1, i)

N, K = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(1, N):
    arr[i] = arr[i-1] + arr[i]

P = [0]*2
res= 0
DFS(0, 1)
print(res+arr.count(K))


"""
import sys
from itertools import combinations
input = sys.stdin.readline


N, K = map(int, input().split())
arr = list(map(int, input().split()))
res = arr.count(K)
for i in range(1, N):
    arr[i] = arr[i-1] + arr[i]

for com in combinations(range(1, N), 2):
    s = arr[com[1]] - arr[com[0]-1]
    if s == K:
        res += 1
        
print(res + arr.count(K))
