N = int(input())
nums = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    while  x >0:
        sum += x%10 #10으로 나눈 나머지 합하기
        x = x//10 #몫
    return sum
max = -2147000000
for n in nums:
    tot = digit_sum(n)
    if tot > max:
        max = tot
        res = n
print(res)



""" String -> list -> index, sum -> dictionary -> 내림차순 정렬
di = {}
def digit_sum(x):
    return sum(x)

for i in range(N):
    num = list(map(int, str(nums[i])))
    di[i] = digit_sum(num)

aws = sorted(di.items(), key=lambda x: x[1], reverse= True)
print( nums[aws[0][0]])
"""


"""
dictionay 정렬 !!
 - value별 정렬
    sorted(di.items(), key=lambda x: x[1], reverse= True) => tuple로된 리스트 return
    sorted(di.keys()) => key로 오름차순 정렬
    sorted(di.items()) => key로 오름차순 정렬 / tuple로 묶어서 정렬
"""



"""
3
125 15232 97
"""