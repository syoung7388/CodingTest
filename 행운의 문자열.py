import sys
def DFS(c, L):
    if L == N:           
        return 1
    
    r = 0
    
    for k in dic.keys():
        if c != k and dic[k] != 0:
            dic[k] -= 1
            r += DFS(k, L+1)
            dic[k] += 1
     
    return r    
S = input()
N = len(S)
dic = {}
t = set(S)

if len(S) == 10:
    if len(t) == 10:
        print(3628800)
        sys.exit(0)
    elif len(t) == 9:
        print(1451520)
        sys.exit(0)

for s in S:
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1

print(DFS(None, 0))

    
