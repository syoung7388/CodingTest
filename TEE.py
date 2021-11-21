import sys
input = sys.stdin.readline
import heapq

sys.setrecursionlimit(100000)

def find(x):
    if head[x] == x:
        return head[x]
    head[x] = find(head[x])
    return head[x]


def union(a, b):
    global S
    x = find(a)
    y = find(b)
    if x == y: return 0
    if x < y:
        head[y] = x
        head[b] = x
        S -= nC2(counter[x])
        S -= nC2(counter[y])
        counter[x] += counter[y]
        return x

    else:
        head[x] = y
        head[a] = y
        S -= nC2(counter[x])
        S -= nC2(counter[y])
        counter[y] += counter[x]
        return y
    
def nC2(a):
    return a*(a-1)// 2
        

N, M = map(int, input().split())
H = []
tot = 0
for _ in range(M):
    a, b,v = map(int, input().split())
    heapq.heappush(H, (-v, a, b))
    tot += v


head = [x for x in range(N+1)]
counter = [1]*(N+1)


res = 0
S = 0
for _ in range(M):
    v, a, b = heapq.heappop(H)
    h = union(a, b)
    if counter[h] == N: break
    if h:
        S += nC2(counter[h])
    res += S*(-v)
    tot += v

res += tot*nC2(N)
print(res)

