import sys

def update(i, a):
    
    while i <= n:
        tree[i] += a
        i += (i&-i)
    
def subSum(i):
    res = 0
    while i > 0:
        res += tree[i]
        i -= (i&-i)
    return res

n, q = map(int, input().split())
arr = [0]+ list(map(int, input().split()))
tree = [0]*(n+1)


for i in range(1, n+1):
    update(i, arr[i])
    
for _ in range(q):
    s, e, a, b = map(int, input().split())
    
    print(subSum(e)-subSum(s-1))

    diff = b - arr[a]
    arr[a] = b

    update(a, diff)
    
    
