

import re

r = re.compile('(10+1+|01)+')
for _ in range(int(input())):
    i = input()
    s = r.fullmatch(i)
    if s :
        print("YES")

    else:
        print("NO")
