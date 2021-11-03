import sys
input = sys.stdin.readline

import sys
input = sys.stdin.readline
def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

    
def union(a, b):
    a = find(a)
    b = find(b)
    parent[a] = b

N, M = map(int, input().split())

parent = [x for x in range(M+1)]

arr = [0]*(M+1)
for i in range(N):
    a, b = map(int, input().split())
    res = "LADICA"
    if not arr[a]:
        print("A직행")
        arr[a] = 1
        union(a, b)
    elif not arr[b]:
        
        print("B직행")
        arr[b] = 1
        union(b, a)
    elif not arr[find(a)]:
        print("A 대가리로 직행")
        arr[find(a)] = 1
        union(a, b)
    elif not arr[find(b)]: 
        print("B 대가리로 직행")
        arr[find(b)] = 1
        union(b, a)
    else:
        res = "SMECE"
    print(arr)
    print(parent)

    print(res)


    
            
#print(parent)              
