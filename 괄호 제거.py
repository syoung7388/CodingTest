def DFS(L):
    if L == len(ho):
        r = ''.join(arr)
        res.add(r)
        return
    arr[ho[L][0]] = ""
    arr[ho[L][1]] = ""
    DFS(L+1)
    arr[ho[L][0]] = "("
    arr[ho[L][1]] = ")"
    DFS(L+1)

arr = list(map(str, input()))
N = len(arr)
ho = []
stack = []


for i in range(N):
    if arr[i] == '(':
        stack.append(i)
    elif arr[i] == ')':
        ho.append((stack.pop(), i))
        
res = set()
DFS(0)

res = list(res)

res.remove(''.join(arr))
res.sort()
for r in res:
    print(r)
