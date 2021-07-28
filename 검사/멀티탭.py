from collections import deque


N,K = map(int, input().split())
item = deque(map(int, input().split()))
tab = [0]*N
maxIndex =-1
out = 0
cnt = 0

while item:
    q = item.popleft()
    if q in tab:
        continue
    elif 0 in tab:
        tab[tab.index(0)] = q
    else:
        cnt += 1
        for i in range(N):
            if tab[i] not in item:
                out = i
                break
            elif item.index(tab[i]) > maxIndex:
                maxIndex = item.index(tab[i])
                out = i
        tab[out] = q
        maxIndex = -1
        out = 0
                    
print(cnt)

                
            
