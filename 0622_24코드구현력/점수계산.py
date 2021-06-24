N= int(input())
scores = list(map(int, input().split()))
plus= 0
aws = 0
for s in scores:
    if s == 1:
        plus += 1
        aws += plus
    else: # 만약에 b=0 이라면 원복
        plus = 0
print(aws)
