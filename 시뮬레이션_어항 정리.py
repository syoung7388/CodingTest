from collections import deque
from collections import defaultdict
import sys
input = sys.stdin.readline

def control(gra):
    temp = defaultdict(int)
    n, m = len(gra), len(gra[0])
    
    for x in range(n):
        for y in range(m):
            if gra[x][y] == -1: continue
            for a, b in [(1, 0), (0, 1)]:
                xx, yy = a + x, y+b
                if not (0<=xx<n and 0<=yy<m) or gra[xx][yy] == -1: continue
                diff = abs(gra[xx][yy]-gra[x][y])//5
                if diff == 0: continue
                a, b = diff, diff
                if gra[xx][yy] > gra[x][y]:
                    b = -b
                else:
                    a= -a


                temp[(xx, yy)] += b
                temp[(x, y)] += a


    for k, v in temp.items():
        gra[k[0]][k[1]] += v



    n_arr = []
    for i in range(n):
        for j in range(m):
            if gra[i][j] == -1: break
            n_arr.append(gra[i][j])
    return n_arr
        
    
    
def roll(gra):
    order = [0]
    while True:
        n_order = []
        a = order[-1] + 1
        n = len(gra[order[0]])
        m = len(order)
        if a + n > N: break #삐쳐나가면 break
        for i in range(n):
            for j in range(m-1, -1, -1):
                gra[a+i].append(gra[order[j]].popleft())
            n_order.append(a+i)
        order = n_order
    l = len(gra[order[0]])   
    return control([list(gra[i])+[-1]*(l-len(gra[i])) for i in range(order[0], N)])

            
def turn():

    n = N//4
    gra =[]


    for i in range(0, N, n):
        gra.append(arr[i:i+n])

    gra[2].reverse()
    gra[0].reverse()
    gra = [gra[2], gra[1], gra[0], gra[3]]
    
    gra = list(map(list, zip(*gra)))
    for i in range(len(gra)):
        gra[i].reverse()
    
    return control(gra)


N, K = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

        
while True:

    mini = min(arr)
    for i in range(N):
        if mini == arr[i]:
            arr[i] += 1


    gra = [deque([a]) for a in arr]
    arr = roll(gra)
    arr = turn()
    cnt += 1
    if max(arr) - min(arr) <= K:break
print(cnt)
