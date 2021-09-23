
N = int(input())

time = [list(map(int, input().split())) for _ in range(N)]

time.sort(key = lambda x: -x[1])
remain = time[0][1] - time[0][0] #20시 - 5시 = 15시간
for i in range(1, N):
    if remain > time[i][1]:
        remain = time[i][1] - time[i][0]
    else:
        remain -= time[i][0]
if remain >= 0:
    print(remain)
else:
    print(-1)



""" #이분탐색 방법 100초

def Check(mid):
    cur = mid
    for i in range(N):
        cur += time[i][0]
        if cur > time[i][1]:
            return False
    return True



N = int(input())
time = [list(map(int, input().split())) for _ in range(N)]

lt = 0
rt = time[-1][1]
res = -1
while lt <= rt:
    mid = (lt+rt)//2
    if Check(mid):
        res = max(mid, res)
        lt = mid+ 1
    else:
        rt = mid-1
print(res)
"""
