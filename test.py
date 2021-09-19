L, R = map(str, input().split())

llen = len(L)
rlen = len(R)

cnt = 0
if llen != rlen:
    print(cnt)
    break
else:
    for l in range(llen):
        if L[l] != R[l]:
            break
        if L[l] == '8':
            cnt += 1
    print(cnt)
            
    
