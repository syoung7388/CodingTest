N = int(input())
zu = list(map(int, input().split()))



arr = []
arr.append(min(zu[0], zu[5]))
arr.append(min(zu[1], zu[4]))
arr.append(min(zu[2], zu[3]))
arr.sort()

res = 0

len3 = sum(arr)
len2 = arr[0]+arr[1]
len1 = arr[0]

cnt3 = 4
cnt2 = (N-2)*4 + (N-1)*4
cnt1 = (N-2)*(N-2) + (N-2)*(N-1)*4


res += (cnt1*len1 + cnt2*len2 + cnt3*len3)
print(res)
