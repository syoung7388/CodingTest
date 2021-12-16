from collections import defaultdict
import sys
input = sys.stdin.readline

def roll(gra):
    order = [0]
    
    while True:
        a = order[-1]       
        n = len(gra[order[0]]) #몇명에게 쌓이는지
        m = len(order) #쌓이는 칸수 (idx)
        if (a + n) >= N: break
        n_order = []
        for i in range(n): 
            for j in range(m-1, -1, -1):
                gra[a+i+1].append(gra[order[j]].pop(0))
            n_order.append(a+i+1)
        order = n_order


    l = len(gra[order[0]])
    gra = [gra[i]+[-1]*(l-len(gra[i])) for i in range(order[0], N)]

    return control(gra)

def control(gra):
    n, m  = len(gra), len(gra[0])
    fish_mv = defaultdict(int)
    for x in range(n):
        for y in range(m):
            if gra[x][y] == -1: continue
            for a, b in [(0, 1), (1, 0)]:
                xx, yy = x+a, y+b
                if not (0<=xx<n and 0<=yy<m) or gra[xx][yy] == -1: continue
                diff = abs(gra[xx][yy] - gra[x][y]) // 5

                if diff == 0: continue
                c, d = diff, diff
                if gra[xx][yy] > gra[x][y]: d = -d
                else: c = -c

                fish_mv[(xx, yy)] += d
                fish_mv[(x, y)] += c
    
    for k, v in fish_mv.items():
        gra[k[0]][k[1]] += v

    n_arr = []
    for i in range(n):
        for j in range(m):
            if gra[i][j] == -1: break
            n_arr.append(gra[i][j])
    return n_arr
                
                
        
def turn(arr):
    n = N//4
    one = arr[:n]
    two = arr[n:2*n]
    three = arr[2*n:3*n]
    four = arr[3*n:]
    one.reverse()
    three.reverse()


    z = list(map(list, zip(four, one, two, three)))
    return control(z)
    
    
    
#main
N, K = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0


while True:
    #1)
    mini = min(arr)
    for i in range(N):
        if arr[i] == mini:
            arr[i] += 1
   #2) 공중부양, 정리, 일렬
    gra = [[a] for a in arr]
    arr = roll(gra)

    #3) N//4 turn
    arr = turn(arr)

    cnt += 1
    if max(arr) - min(arr) <= K: break
print(cnt)

