from collections import defaultdict
from datetime import datetime, timedelta
import sys
input = sys.stdin.readline

n, limit, money = map(str, input().split())
n, money = int(n), int(money)



a, b= limit.split('/')
h, m = b.split(":")
limit = timedelta(days = int(a), hours = int(h), minutes = int(m))

dic = defaultdict(lambda : defaultdict(int))
fine = 0
res = defaultdict(int)

for i in range(n):
    arr = list(map(str, input().split()))

    time = datetime.strptime(arr[0]+" "+arr[1], '%Y-%m-%d %H:%M')


    if arr[2] in dic and arr[3] in dic[arr[2]]:
        cha = ((time - dic[arr[2]][arr[3]]) - limit).total_seconds()
        if cha > 0:
            res[arr[3]] += (cha//60)*money
        
        del dic[arr[2]][arr[3]]
    else:
        dic[arr[2]][arr[3]] = time
if len(res) == 0:
    print(-1)
else:
    for name, f in sorted(res.items()):
        print(name, int(f))
