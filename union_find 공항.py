import sys
input = sys.stdin.readline

#시간복잡도: O(P)  
#P =100000 O(NlogN) 까지 가능 -> O(N)이라서 가능 함 !!
def find(x):
    global arr
    arr += 1
    if head[x] == x:
        return x
    head[x] = find(head[x])
    return head[x]
G = int(input())
P = int(input())
gate = [0]*(G+1)
head = [x for  x in range(G+1)] 
head[1] = 1
cnt = 0
gate[0] = 1
for i in range(P): #O(P)
    a = int(input())
    arr = 0
    d = find(a) # O(1)
    if d == 0:
        break
    head[d] = head[d-1]
    cnt += 1
