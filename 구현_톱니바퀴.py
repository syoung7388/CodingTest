from collections import deque
import sys

def left_turn(n):
    gra[n].append(gra[n].popleft())

def right_turn(n):
    gra[n].appendleft(gra[n].pop())

gra = [deque(map(int, sys.stdin.readline().rstrip())) for _ in range(4)]

K = int(input())

for _ in range(K):
    num, d = map(int, sys.stdin.readline().split())
    ch = [0]*(4)
    ch[num-1] = d
    for i in range(num-1, 3):
        if gra[i][2] != gra[i+1][6]:
            ch[i+1] = -ch[i]
    for i in range(num-1, 0, -1):
        if gra[i][6] != gra[i-1][2]:
            ch[i-1] = -ch[i]

    
    for idx, nd in enumerate(ch):
        
        if nd == -1:
            left_turn(idx)
        if nd== 1:
            right_turn(idx)

res = 0
if gra[0][0] == 1:
    res += 1
if gra[1][0] == 1:
    res += 2
if gra[2][0] == 1:
    res += 4
if gra[3][0] == 1:
    res += 8

print(res)
        
 
