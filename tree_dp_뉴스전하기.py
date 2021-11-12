import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def Send(h):
    global cnt
    cnt += 1
    if not G[h]:
        return 0
    arr = []
    for g in G[h]: 
        arr.append(Send(g))

    arr.sort(reverse=True)
    for i in range(len(arr)):
        arr[i] += i+1
    return max(arr)
        

N = int(input())
G = [[] for _ in range(N+1)]
arr = list(map(int, input().split()))
for a in range(1, N):
    G[arr[a]].append(a)
cnt = 0
print(Send(0))
print(cnt)
