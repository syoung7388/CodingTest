""" 완전 탐색 (가능한 경우의수를 모두 탐색)
입력값 N
시간 : 00시 00 분 00초 ~ N시 59분 59초까지의 시각중 N이 포함될 경우의 수
완전탐색 유형 !!
핵심 입력값 = 시간 = 서칭값
"""

h = int(input())
count = 0
for H in range(h+1):
    for M in range(60):
        for S in range(60):
            if '3' in str(H)+str(M)+str(S):
                count += 1
print(count)

