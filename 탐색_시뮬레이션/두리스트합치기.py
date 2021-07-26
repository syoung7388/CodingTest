N= int(input())
ns = list(map(int, input().split()))
M = int(input())
ms = list(map(int, input().split()))
p1=p2= 0
c = []
while p1 > N or p2 > M :
    if ns[p1] <= ms[p2]:
        c.append(ns[p1])
        p1 += 1
    else:
        c.append(ms[p2])
        p2 += 1
if p1 < N:
    c = c+ ns[p1:]
if p2 < M:
    c= c+ ms[p2:]
for i in c:
    print(i, end=" ")
