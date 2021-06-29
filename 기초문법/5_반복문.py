'''
홀수
합
약수
'''
num = int(input())
sum = 0

for i in range(1, num+1):
    if i%2==1:
        print(i, end=" ")

for i in range(1, num+1):
    sum += i
print(sum)


for i in range(1, num+1):
    if num%i==0:
        print(i, end=" ")
