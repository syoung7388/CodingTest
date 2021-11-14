import sys
input  = sys.stdin.readline


def make_tree(t, st, ed):
    if  st == ed:
        tree[t] = arr[st]
        return tree[t]
    mid = (st+ed)//2
    tree[t] = make_tree(t*2,st,mid)+make_tree(t*2+1, mid+1, ed)
    return tree[t]

def subSum(t, st, ed, left, right):
    if st > right or ed < left: return 0 #겹치지 X
 
    if left <= st and ed <= right: return tree[t]
    
    
    mid = (st+ed)//2
    return subSum(t*2, st, mid, left, right) +subSum(t*2+1, mid+1, ed, left, right)


def update(t, st, ed, idx, diff):

    if st > idx or ed < idx: return

 

    tree[t] += diff
    if st != ed:
        mid = (st+ed)//2
        update(t*2, st, mid, idx, diff)
        update(t*2+1, mid+1, ed, idx, diff)

    

    
    
n, q = map(int, input().split())
arr = list(map(int, input().split()))

tree = [0]*(n*4)
make_tree(1, 0, n-1)

for _ in range(q):
    s, e, a, b = map(int, input().split())
    if s > e:
        s, e = e, s

    print(subSum(1, 0, n-1, s-1, e-1))

    diff = b - arr[a-1]
    arr[a-1] = b
    update(1, 0, n-1, a-1, diff)

    
