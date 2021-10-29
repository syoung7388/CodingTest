import sys
input = sys.stdin.readline


def check(mid):

    P = N-1
    for i in range(mid, M):
        if pizza[P] > oven[i]:
            return False
        P -= 1
        if P == -1:
            return True
    return False
    

M, N = map(int, input().split()) #오븐 깊이, 피자개수
oven = list(map(int, input().split())) #오븐 최상단 부터
pizza = list(map(int, input().split())) #피자만들어지는 순서대로




for i in range(1, M):
    oven[i] = min(oven[i-1], oven[i])


res= -1
lt ,rt = 0, M-1

while lt <= rt:

    mid = (lt+rt)//2

    if check(mid):
        res = mid
        lt = mid+1
    else:
        rt = mid -1

if res == -1:
    print(0)
else:
    print(res + 1)

