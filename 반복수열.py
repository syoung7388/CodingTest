
"""

import sys

def DFS(num):
    res.append(num)
    S = 0
    n = num
    global cut
    for _ in range(len(str(num))):
        S += (n%10)**p
        n = n//10
    if S in res:
        cut = S
        return
    else:
        DFS(S)
if __name__ == "__main__":

    A, p = map(int, input().split())
    res = list()
    cut = 0
    DFS(A)

    res = res[0:res.index(cut)]
    print(len(res))
"""



a, p = input().split()
p = int(p)
pows = {str(i):i**p for i in range(10)}
check = {a:0}
j = 0

while True:
    a = str(sum(pows[j] for j in a))
    if a in check:
        print(check[a])
        break
    else:
        j+=1
        check[a] = j

    
