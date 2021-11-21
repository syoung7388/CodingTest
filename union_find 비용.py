import sys 
input = sys.stdin.readline

def nC2(x):
    return x*(x-1)//2
def find(x):
    if head[x] == x:
        return head[x]
    head[x] = find(head[x])
    return head[x]

def union(a, b):
    global S
    a = find(a)
    b = find(b)
    if a == b: return  

    #합치기 전에 중복 방지를 위해서
    S -= nC2(counter[a])
    S -= nC2(counter[b])
    if a < b:
        head[b] = a
        counter[a] += counter[b]
        S += nC2(counter[a])
    else:
        head[a] = b
        counter[b] += counter[a]
        S += nC2(counter[b])
      

N, M = map(int, input().split())
sun = [list(map(int, input().split())) for _ in range(M)]
sun.sort(key = lambda x : x[2], reverse = True)
counter = [1]*(N+1)
head= [x for x in range(N+1)]
S = 0
res = 0
for a, b, v in sun:
    union(a, b)
    res += S*v

if res > 10**9:
    print(res%10**9)
else:
    print(res)
