import sys
input = sys.stdin.readline


def f(a, l, d):
    return (l-a)/d+1


def count(mid):
    cnt = 0
    for s, e, p in rule:
        if mid < s:
            break
        cnt += int(f(s, min(mid, e), p))
    #print("m:", mid, "개수:",cnt)
    return cnt 


N, K, D = map(int, input().split())

rule = [list(map(int, input().split())) for _ in range(K)]
rule.sort()
lt = rule[0][0]
rt = N #상자의 개수

while lt <= rt:
    
    mid = (lt+rt)//2
    if count(mid) < D:
        lt = mid + 1
    else:
        res = mid
        rt = mid-1
        
print(res)
