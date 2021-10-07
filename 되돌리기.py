import sys
input = sys.stdin.readline
N = int(input())
dic = dict()
bf = 0
dic[0] = ""
for i in range(N):
    order, s, sec = map(str, input().split())
    sec = int(sec)
    if order == 'type':
        dic[sec] = dic[bf] + s
    elif order == 'undo':
        s = int(s)
        time = max(sec-s-1, 0)
        if time in dic:
            dic[sec] = dic[time]
        else:
            for k in sorted(dic.keys(), reverse = True):
                if k < time:
                    dic[sec] = dic[k]
                    break
    bf = sec

print(dic[bf])
