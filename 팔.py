L,R = map(str, input().split())

lt, rt = len(L), len(R)
cnt = 0

if lt != rt:
    print(cnt)
else:
    for i in range(lt):
        if L[i] != R[i]:
            break
        else:
            if L[i] == '8':
                cnt += 1
    print(cnt)
