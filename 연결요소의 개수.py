import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
ch = [0]*M
m = [list(map(int, input().split())) for _ in range(M)]
cnt = 0
wonso = set(m[0])
ch[0] = 1
flag = False
while True:
    if flag == True:
        break
    for i in range(1, M):
        print(ch)
        if all(str(ch[i])):
            flag = True
        if ch[i] != 0: continue
        if m[i][0] in wonso or m[i][1] in wonso:
            ch[i] = 1
            wonso.add(m[i][0])
    wonso.clear()
    cnt += 1
    print(wonso)
        
            
print(cnt)      
            

