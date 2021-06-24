# 평균구하기
# 평균에 가까운 점수들 찾기
# 점수 높은거 찾기
#학생 번호 낮은거 찾기

N = int(input())
S = list(map(int, input().split()))
avg = int(sum(S)/N+0.5)
min = 2147000000
for idx, s in enumerate(S):
    tmp = abs(avg -s)
    if tmp < min:
        min = tmp
        i = idx+1
        score = s
    elif tmp == min:
        if s > score:
            i = idx+1
            score = s
print("%d %d" %(avg, i))


"""
SS = sorted(S)
bf = SS[0]
for s in range(1,len(SS)):
    if abs(avg - SS[s]) == abs(avg - bf):
        bf = (SS[s] if SS[s] > bf else bf)
    elif abs(avg - SS[s]) < abs(avg - bf):
        bf = SS[s]
    print("%d %d"%(avg, S.index(bf)+1))
"""







"""
10
45 73 66 87 92 67 75 79 75 80
"""


