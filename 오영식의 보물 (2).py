#temp로 옮기는거 따로 | 목적지로 옮기는거 따로

    
def Hanoi(n, s, e, temp):
    if n == 0:
        return 
    if n == 1:
        arr[arr.index(s)] = e
        tem.append(''.join(arr))
        return
    Hanoi(n-1, s, temp, e)
    arr[arr.index(s)] = e
    tem.append(''.join(arr))
    Hanoi(n-1, temp, e, s)



N, M = map(int, input().split())
last = list(map(str, input()))



arr = ['A']*N

ch = [0]*N
res = ['A'*N]
cnt = 0

anw = []

#AAAAAA
for i in range(N-1, -1, -1):
    s = arr[i]
    e = last[i]
    tem = []
    if s == e: continue
    ch[ord(s)-65],ch[ord(e)-65] = 1, 1

    temp =chr(ch.index(0)+65)
    ch[ord(s)-65],ch[ord(e)-65] = 0, 0
    wi = arr[:i].count(arr[i])

    
    Hanoi(wi, s ,temp, e)
    arr[i] = e
    tem.append(''.join(arr))
    cnt += len(tem)
    
    #print(cnt)
    #print(tem)
    if cnt == M:
        anw = tem[-1]
        break
    elif cnt > M:
        #print(abs((cnt-M)-len(tem)) -1)
        anw = tem[abs((cnt-M)-len(tem))-1]
        break
    


if M == 0:
    print(res[0])
else:
    print(anw)

