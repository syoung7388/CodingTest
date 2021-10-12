from collections import deque

A, B = map(int, input().split())

Q = deque([(A, 1)])
ch = set()

res = -1
while Q:
    X, cnt = Q.popleft()
    if X == B:
        res = cnt
    if X*2 <= B and X*2 not in ch:
        ch.add(X*2)
        Q.append((X*2, cnt+1))
    if X*10 + 1 <= B  and  X*10 + 1 not in ch:
        ch.add(X*10+1)
        Q.append((X*10 + 1, cnt+1))
print(res)
