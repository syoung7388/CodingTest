import sys
S = list(input())

N = len(S)
arr = []
res = 0
for i in range(N):


    #44(22233)
    
    if S[i] == '(':
        arr.append('(')
    elif S[i] == ')':
        res = 0
        

        #'(' 22233 -> 이 숫자들 길이 측정
        while True:
            if arr[-1] == '(':
                break
            if len(arr[-1]) == 2:
                res += arr[-1][1]
            else:
                res += 1
            arr.pop()

        arr.pop() #'(' pop()
        
        res *= int(arr.pop()) #앞에 있는 4곱해주기
        

        #나머지 숫자 더해주기
        while arr:
            if arr[-1] == '(' or len(arr[-1]) == 2:
                break
            res += 1
            arr.pop()

            
        #괄호안에꺼 다 청산한 후 append
        arr.append((0, res))

    else:
        arr.append(S[i])
res = 0


for a in arr:
    if len(a) == 2:
        res += a[1]
    else:
        res += 1
print(res)
