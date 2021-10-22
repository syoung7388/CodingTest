def Print(a):
    for i in a:
        print(chr(i+65), end = " ")
    print()
    
def Ha(n, f, t, temp):
    #print("n:", n, "f:", f, "t:", t, "temp:", temp)
    if arr[arrive[0]] == arrive[1]:
        return
    if n == 1:
        arr[arr.index(f)] = t
        Print(arr)
        res.append(arr[:])
        return
    Ha(n-1, f, temp, t)
    arr[arr.index(f)] = t
    Print(arr)
    res.append(arr[:])
    Ha(n-1, temp, t, f)
    



N, M = map(int, input().split())

st = list(map(str, input()))

arr= [0]*N
res = [arr[:]]
for i in range(N-1, -1, -1):
    f = arr[i]
    t = ord(st[i]) - 65
    if f == t:continue
    temp = list(filter(lambda x : not x in [f, t], [0, 1, 2]))
    n = 0
    for j in range(i+1):
        if arr[j] == f:
            n += 1
    arrive = [i, t]
    print(n, f, t, "=================")
    Ha(n, f, t, temp[0])
    print(len(res))
    #print(arr)

for r in res[M]:
    print(chr(r+65), end = "")

print()
for r in res:
    for i  in r:
        print(chr(i+65), end = " ")
    print()

