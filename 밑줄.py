# 반성점: 문제에서 '순서대로 이어 붙이고'를 보지 못했고 그래서 시간이 엄청 걸렸다.
# 오늘의 교훈: 문제 습득력도 너의 재주다. 뭔가 이상하다 싶을때 다시 문제 읽기! 


N, M = map(int, input().split())
words = []
S = 0
for _ in range(N):
    word = input()
    S += len(word)
    words.append(word)


ch = [0]*(N) #1번단어랑 비교, 2번 단어랑 비교, 3번단어랑 비교

center = ord("_")

base = (M-S) // (N-1)
plus = (M-S) % (N-1)

res = words[0]
for i in range(1, N):
    if (N-i-1) < plus:
        plus -= 1
        res += "_"*(base+1)
    elif plus == 0:
        res += "_"*(base)
    elif ord(words[i][0]) < center: #뒤에 남은 숫자들
        res += "_"*(base)
    elif ord(words[i][0]) > center:
        plus -= 1
        res += "_"*(base+1)
    res += words[i]


print(res)
        

    






