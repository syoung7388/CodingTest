import sys
input = sys.stdin.readline

def T(n):
    if len(tree[n]) == 1:
        if tree[n][0] != n:
            T(tree[n][0])
            tree[n] = tree[tree[n][0]] 
        return
    else:
        left, right = tree[n][0], tree[n][1]
        T(left)
        T(right)
        if len(tree[left]) == 0 and len(tree[right]) == 0: return
        flag = False
        l,r = len(tree[left]), len(tree[right])
        if l > r:
            m = l
            flag = True
        else:
            m = r
        arr = []
        for i in range(m):
            if flag:
                arr.append(tree[left][i])
                arr.append(tree[right][i%r])
            else:
                arr.append(tree[left][i%l])
                arr.append(tree[right][i])
        tree[n] = arr
        return 
    
    
    
    
N = int(input())
tree = [[] for _ in range(N+1)]
for i in range(1, N+1):
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        tree[i].append(i)
        continue
    if a == -1 and b != -1:
        tree[i].append(b)
    elif a != -1 and b == -1:
        tree[i].append(a)
    else:
        tree[i] += [a,b]

T(1)
T = int(input())
t = len(tree[1])
print(tree)
print(tree[1][(T-1)%t])
    
