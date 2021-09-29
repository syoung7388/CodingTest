long = list(map(int, input().split()))
short = list(map(int, input().split()))

L = len(long)
S = len(short)

tot = L+S+S-2
ch = [0]*tot
minlen = L+S-1

for i in range(L):
    ch[i+S-1] = long[i]

for i in range(tot-S):#0 ~ 15
    arr = ch[:]
    for j in range(S):
        if arr[i+j] + short[j] == 4:
            break
        arr[i+j] = 3
    else:
        idx = [x for x in range(tot) if arr[x]]
        minlen = min(minlen, max(idx)-min(idx))
    
print(minlen+1)
