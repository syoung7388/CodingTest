
def getRes(x, y, dy):
    r = 2147000000
    print("=========")
    for i in range(x+1, y):
        print(i, end=" ")
        if dy[i-1]&dy[i] == 0:   
            return 0
        else:
            r = min(dy[i-1]&dy[i],r)
    print(r)
    return r
                

def solution(m, b):
    res = []
    cnt = 0
    for k in m:
        res.append(getRes(cnt,k+cnt, b))
        cnt += k
    return res


print(solution([2,5],[3,2,1,9, 1, 3, 4 ]))


print(9&1&3&4)
