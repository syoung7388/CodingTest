def DFS(L, s, mo, ja):
    if L == N:
        if mo >= 1 and ja >= 2:
            print(''.join(P))
        return
    for i in range(s+1, 27):
        if ch[i] == 0: continue
        P[L] = chr(i+96)
        ch[i] -= 1
        if chr(i+96) in 'aeiou':
            DFS(L+1, i, mo+1, ja)
        else:
            DFS(L+1, i, mo, ja+1)
        ch[i] += 1
        







N, M = map(int, input().split())
ch= [0]*27
for i in list(map(str, input().split())):
    ch[ord(i)-96] += 1
P = [0]*N

DFS(0, 0, 0, 0)
