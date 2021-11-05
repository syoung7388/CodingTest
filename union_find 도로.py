import sys
input = sys.stdin.readline

def find(x):
    if head[x] == x:
        return x
    head[x] = find(head[x])
    return head[x]

def union(a, b):
    a = find(a)
    b = find(b)
    head[b] = a
    



N, M = map(int, input().split())
gra = [input() for _ in range(N)]
Yes = []
No = []
cnt = 0
head = [x for x in range(N)]
for i in range(N):
    for j in range(i+1, N):
        if gra[i][j] == 'Y':
            if find(i) != find(j):
                Yes.append((i, j))
                cnt += 1
                union(i, j)
            else:
                No.append((i, j))
                
if cnt == N-1 and len(Yes) + len(No) >= M:
    res = [0]*N
    for x, y in Yes:
        res[x] += 1
        res[y] += 1
    for i in range(M-(N-1)):
        res[No[i][0]] += 1
        res[No[i][1]] += 1
    print(' '.join(map(str, res)))
    
else:
    print(-1)
        

            
