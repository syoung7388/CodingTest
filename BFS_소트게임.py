from collections import deque

def change(i, s):
    s = list(map(str, s))
    n = K+i-1
    for j in range(K//2):
        s[i], s[n] = s[n], s[i]
        n-=1
        i+=1
    return ''.join(s)
N, K = map(int, input().split())
arr = list(input().split())
res = "".join(sorted(arr))
arr = "".join(arr)
ch = set([arr])

Q = deque([(0, arr)])

anw = -1
while Q:
    cnt, s = Q.popleft()
    if res == s:
        anw = cnt
        break
        
    for i in range(N-K+1):
        temp = change(i, s)
        if not temp in ch:
            ch.add(temp)
            Q.append((cnt+1, temp))

print(anw)


