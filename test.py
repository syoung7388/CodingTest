import sys
input = sys.stdin.readline


def find(x):
    if head[x] == x:
        return x
    #head[x] = find(head[x])
    return find(head[x])
def union(a, b):
    a = find(a)
    b = find(b)
    head[b] = a

G = int(input())
P = int(input())

gate = [0]*(G+1)
head = [x for  x in range(G+1)]
head[1] = 1
cnt = 0
gate[0] = 1
p = ["아시아나", "대한항공", "에어부산", "제주항공", "티웨이"]
for i in range(P):
    a = int(input())
    if gate[a] == 0:
        gate[a] = p[i]
    else:
        #print(find(a-1))
        if gate[find(a)] == 0:
            gate[find(a)] = p[i]
        else:
            break


    a = find(a)
    if a-1 != 0 and find(a-1) != find(a):
        union(a-1, a)
    #print(gate)
    #print(head)
    
    cnt += 1
    
print(cnt)
