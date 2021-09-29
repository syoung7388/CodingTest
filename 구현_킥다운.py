long = list(map(int, input()))
short  = list(map(int, input()))

L = len(long)
S = len(short)
tot = S+L+S-2
ch = [0]*(tot)

#출발점 = 0 ~ 16 (L+S -1) 
# short 출발점 ~ short + short 길이 -1

mincnt = S+L-1

for i in range(L):
    ch[S+i-1] = long[i]
    
for i in range(tot-S): #0,1,2,3 ... 16

    tmp = ch[:]
    for j in range(S): #0, 1, 2, 3, 4, 5, 6
        if short[j]+ ch[i+j] == 4:
            break
        tmp[i+j] = 3
    else:
        idx = [i for i in range(tot) if tmp[i]]
        mincnt = min(mincnt, max(idx) - min(idx))
print(mincnt+1)
