"""
S = "0< <9"
X or + 를 넣어 만들어 질 수 있는 가장 큰수

1.0,1 경우 더하기 수행
나머지 곱하기 수행

2.String int로 변경

3. [0]-[1] /// -[2] /// -[3]

"""
S = "02984"
result = int(S[0])
for i in range(1, len(S)):
    num = int(S[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)












