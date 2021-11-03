import sys

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a
        number[a] += number[b]  

for _ in range(int(input())):
    
    parent = {}
    number = {}
    R = []
    cnt = 0
    N = int(input())
    for _ in range(N):
        a, b = map(str, sys.stdin.readline().rstrip().split())
        if a not in parent:
            parent[a] = a
            number[a] = 1

        if b not in parent:
            parent[b] = b
            number[b] = 1

        union(a, b)
        #print(parent)

        print(number[find(a)])
