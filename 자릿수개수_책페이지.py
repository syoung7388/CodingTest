import sys

def change(lt, rt, cnt1, cnt2):
    for i in range(10):
        ch[i] += cnt2
        if lt <=  i <= rt:
            ch[i] += cnt1
        

N = int(input())
ch = [0]*10


if N < 10:
    for i in range(1, N+1):
        ch[i] = 1
    print(" ".join(map(str, ch)))
    sys.exit(0)




S = str(N)
L = len(S)

last = 0
for l in range(int(S[-1])+1):
    ch[l] += 1
    last += 1


first_num = int(S[0])-1
cnt1 = 10**(L-1) 
cnt2 = first_num*(10**(L-2))*(L-1) + (10**(L-1) // 10)*(L-1)
change(1, first_num, cnt1, cnt2)
ch[first_num+1] += last
ch[0] -= int("1"*(L-1))

for j in range(1, L-1):
    n = L - j
    num = int(S[j])
    cnt1 = 10**(n-1)
    cnt2 = num*(10**(n-2))*(n-1)
    change(0, num-1, cnt1, cnt2)

    for a in range(j):
        ch[int(S[a])] += num*(10**(n-1))

    ch[num] += last

print(' '.join(map(str, ch)))
