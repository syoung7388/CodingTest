"""
모험가: N명
최대 몇그룹?

핵심) 문제 파악  모험가(X) >= T(X명)
내림차순
"""
data = list(map(int, input().split()))
data.sort()
print(data)
result = 0
count = 0
for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0
print(result)



