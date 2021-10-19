S = list(map(str, input()))
N = len(S)
A = S.count('a')


cnt = S[:A].count('b')
Min = cnt


for _ in range(N-1):
    if S[0] == 'b':
        cnt += 1
    S.insert(0, S.pop())

    if S[A] == 'b':
        cnt -= 1
    Min = min(cnt, Min)
    
print(Min)
"""
=> 유사문제: 광고삽입
=> 알고리즘 종류 : 슬라이딩 윈도우
=> 원리
[aabbaaab]aaba
- 3개를 변경시켜야함
- cf) 연결 리스트
       aaabbaaabaab
       baaabbaaabaa
           ... 이런 형식으로 pop해서 insert 해줘야함

"""
