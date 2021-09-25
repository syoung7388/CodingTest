def DFS(last, L):
    if L == N:
        return 1
    r = 0
    for key in dic.keys():
        if dic[key] != 0 and last != key:
            dic[key] -= 1
            r += DFS(key, L+1)
            dic[key] += 1
    return r 

S = input()

dic = {}
for s in S:
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1
N = len(S)

print(DFS(None, 0))      
