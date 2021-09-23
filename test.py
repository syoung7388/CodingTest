import sys

def Check(mid):
    v = mid
    for i in range(N):
        v += task[i][0]
        if v > task[i][1]:
            return False
    return True

N = int(input())
task = [list(map(int, input().split())) for _ in range(N)]
#0-걸리는 시간 / 1-데드라인


task.sort(key = lambda x : x[1])

lt = 0
rt = task[-1][1]
res = -1
while lt <= rt:
    mid = (lt+rt)//2
    
    if Check(mid):
        res = mid
        lt = mid+1
    else:
        rt = mid-1
print(res)




