
from itertools import permutations
N = int(input())
arr = list(map(int, input().split()))

maxCnt = 0
for i in set(permutations(arr, N)):
    temp = [0]
    cnt = 0
    for j in i:
        temp.append(temp[-1]+j)
    
    for k in temp:
        if k >= 50:
            break
        if k+50 in temp:
            cnt += 1
    maxCnt = max(cnt, maxCnt)
print(maxCnt)
