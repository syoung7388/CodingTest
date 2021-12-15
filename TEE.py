
import sys
input = sys.stdin.readline
from collections import defaultdict
dx, dy = [0, 0, -1, 0, 1], [0, 1, 0, -1, 0]
def control(st, order):
    temp = defaultdict(int)
    for x in order:
        m1 = len(st[x])
        m2 = len(st[x+1]) if x < order[-1] else 0
        
        for y in range(len(st[x])):
            for k in [1, 4]:
                xx, yy = dx[k]+x, dy[k]+y
                if k == 1 and yy >=m1: continue
                if k == 4 and not (xx <= order[-1] and yy < m2): continue

                diff = abs(st[xx][yy] - st[x][y]) // 5
                if diff == 0: continue
                a, b = diff, diff
                if st[xx][yy] > st[x][y]:
                    b = -b
                else:
                    a = -a
                temp[(xx, yy)] += b
                temp[(x, y)] += a
    for k, v in temp.items():
        st[k[0]][k[1]] += v

   

    n_arr = []
    for i in order:
        while st[i]:
            n_arr.append(st[i].pop(0))

    return n_arr   

def roll(st):

    order = [0]
    while True:
        n_order = []
        a = order[-1] + 1 
        if not (a + len(st[order[-1]]) <= N): break
        for i in range(len(st[order[0]])):
            for j in range(len(order)-1, -1, -1):
                st[a+i].append(st[order[j]].pop(0))
            n_order.append(a+i)
        order = n_order


    if order[-1] != N-1:
        order += [x for x in range(order[-1]+1, N)]

    return control(st, order)
   

            
N, K = map(int, input().split())
arr = list(map(int, input().split()))


cnt = 0
while True:
    #print("=====================")
    #1) 최솟값 += 1
    mini = min(arr)
    for i in range(N):
        if mini == arr[i]:
            arr[i] += 1

    #print("1)최솟값:", arr)
    
    #2)어항 쌓기
    st = [[a] for a in arr]
    arr = roll(st)
    
    #print("어항쌓기:", arr)
    #3) 180도 turn
    gra = [[arr[N - i-1], arr[i]] for i in range(N//2)]
    gra.reverse()
    temp = []
    for i in range(N//4):
        gra[i].reverse()
        temp.append(gra[N//2-i-1]+gra[i])
    temp.reverse()
    #print("180도 회전:", temp)

    arr = control(temp, [x for x in range(N//4)])
    #print("온도조절:", arr)
    cnt += 1
    if max(arr) - min(arr)  <= K: break

print(cnt)
    
