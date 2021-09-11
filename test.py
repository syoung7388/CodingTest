from collections import deque


def change(S, x1, x2):
    S[x1], S[x2] = S[x2], S[x1]
    return ''.join(S)
    

Q = deque()
ch = set()
S = ""

for _ in range(3):
    S += ''.join(list(map(str, input().split())))


Q.append((S, 0))
ch.add(S)

res = -1
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
while Q:
    st, cnt = Q.popleft()
    if st == "123456780":
        res = cnt
        break
    zero = st.index('0')

    x, y = zero//3, zero%3

    for k in range(4):
        xx, yy = x+dx[k], y+dy[k]
        if not (0<=xx<3 and 0<=yy<3): continue

        nst = change(list(st), x*3+y, xx*3+yy)

        if not nst in ch:
            ch.add(nst)
            Q.append((nst, cnt+1))
print(res)   
    
