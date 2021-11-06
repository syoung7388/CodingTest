import sys
input = sys.stdin.readline
def find(x):
    if head[x] == x:
        return x
    temp = find(head[x])
    dis[x] += dis[head[x]]
    head[x] = temp
    return head[x]

def union(a, b):
    head[a] = b
    dis[a] += abs(a-b)%1000
for _ in range(int(input())):
    N = int(input())
    dis = [0]*(N+1)
    head = [x for x in range(N+1)]
    
    
    while True:
        arr = list(map(str, input().split()))
        if arr[0] == "O":
            break
        if arr[0] == 'E':
            r = int(arr[1])
            find(r)
            print(dis[r])
        if arr[0] == 'I':
            a, b = int(arr[1]), int(arr[2])
            union(a, b)
            print(head)
    print(dis)
         
