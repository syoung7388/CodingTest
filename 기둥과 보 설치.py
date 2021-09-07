def check(res):
    for x, y, k in res:
        #기둥인 경우
        if k == 0:
            if y == 0 or (x-1, y, 1) in res or (x, y, 1) in res or (x, y-1, 0) in res:
                continue
            else:
                return False
        #보인 경우
        elif k == 1:
            if (x, y-1, 0) in res or (x+1, y-1, 0)in res or ((x-1, y, 1) in res and (x+1, y, 1) in res):
                continue
            else:
                return False
    return True
def solution(N, frame):
    result = set()
    for f in frame:
        x, y, what, how = f
        if how == 1: #설치
            result.add((x, y, what))
            istrue = check(result)
            if istrue:
                continue
            else:
                result.remove((x, y, what))
        elif how == 0: #삭제
            if (x, y, what) in result:
                result.remove((x, y, what))
                istrue = check(result)
                if istrue:
                    continue
                else:
                    result.add((x, y, what))
   
    result = [list(x) for x in result]
    return sorted(result, key = lambda x: (x[0], x[1], x[2]))
                    
print(solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]] ))
