import itertools
def solution(n, weak, dist):
    weakSize = len(weak)
    weak = weak + [w+n for w in weak]
    minCnt = 2147000000
    for start in range(weakSize): #시작점 1, 5, 6, 10
        for d in itertools.permutations(dist, len(dist)):
            # 1,2,3,4  2,1,3,4 ... 등으로 출발 순서가 구해짐
            cnt = 1 #일단 무조건 한명은 채택임
            pos = start #현재 포지션(1)
            for i in range(1, weakSize):
                nextPos = start + i #다음 포지션(5)
                diff = weak[nextPos] - weak[pos]
                if diff > d[cnt-1]: #지금 채택된 새끼가 못간다는 이야기임
                    pos = nextPos #위치도 다음포지션(5)로 변경
                    cnt += 1 #사람 한명 더 채택
                    
                    if cnt > len(dist):
                        break #모든 애들을 채택해도 안되는 경우 나가리
            if cnt <= len(dist):
                minCnt = min(minCnt, cnt)
    if minCnt == 2147000000:
        return -1
    else:
        return minCnt
