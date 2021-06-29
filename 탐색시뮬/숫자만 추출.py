s = input()
#아스키코드?
res = 0
for i in s:
    if i.isdigit():
        res = res*10 + int(i)
print(res)
cnt = 0
for j in range(1, res+1):
    if res%j == 0:
        cnt += 1
print(cnt)





"""
nums = list()
for i in s:
    if i.isalpha() == False:
        nums.append(i)
aws = int("".join(nums))
count = 0
for j in range(1, aws+1):
    if aws%j == 0:
        count+=1
print(aws)
print()
print(count)


"""
