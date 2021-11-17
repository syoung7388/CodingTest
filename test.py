from datetime import datetime, timedelta
import sys
from collections import defaultdict
input = sys.stdin.readline
import re
rent = defaultdict(lambda : defaultdict(int))

N, limit, fine = map(str, input().split())
fine = int(fine)
ld, lh, lm = re.split('/|:', limit)
limit = timedelta(days =int(ld), hours = int(lh), minutes = int(lm))

res = defaultdict(int)
for _ in range(int(N)):
    date, time, item, name = map(str, input().split())

    now = datetime.strptime(date+" "+time, "%Y-%m-%d %H:%M")
    if item in rent and name in rent[item]:
        cha = ((now-rent[item][name])-limit).total_seconds()
        if cha > 0:
            res[name] += int(cha//60)*fine
        
    else:
        rent[item][name] =now
        
    
if res:
    for r in sorted(res.items()):
        print(r[0], r[1])
else:
    print(-1)
