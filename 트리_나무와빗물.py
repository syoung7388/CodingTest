import sys
input = sys.stdin.readline
   
N, W = map(int, input().split())

cnt = [0]*(N+1)

for _ in range(N-1):
    a, b=  map(int, input().split())
    cnt[a] += 1
    cnt[b] += 1


print(W/(cnt.count(1)))
