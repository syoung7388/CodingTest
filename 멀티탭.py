

from collections import deque

N, K = map(int, input().split())
item = list(map(int, input().split()))
plug = [0]*N
maxIndex = 0
temp = 0
unplugItem = 0

cnt = 0
for i in range(K):
    if item[i] in plug:
        pass
    elif 0 in plug:
        plug[plug.index(0)] = item[i]
    else:
        for j in plug:
            if j not in item[i:]:
                unplugItem = j
                # 뒷쪽에 없으면
                # 가장 우선 수위로 빼야할 아이템
            else:
                #더 뒷쪽에 있는지 체크
                temp = item[i:].index(j)
                if temp > maxIndex:
                    maxIndex = temp
        if unplugItem > 0:
            plug[plug.index(unplugItem)] = item[i]
        else:
            plug[plug.index(item[i+maxIndex])] = item[i]
        cnt += 1
        unplugItem = 0
        maxIndex = 0
print(cnt)
        
            
                
                

                
            
