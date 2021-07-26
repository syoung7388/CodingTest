arr = list(map(str, input()))
stack = list()
S = 0
stay = 1
res =0 


for i in range(len(arr)):
    if arr[i] == '(':
        stack.append((2,'('))
    elif arr[i] == '[':
        stack.append((3 ,'['))

    if len(stack) > 0 and (arr[i] == ')' or arr[i] == ']'):
        now = stack.pop()
        if arr[i] == ')' and now[1] != '(':
            print(0)
            break
        if arr[i] == ']' and now[1] != '[':
            print(0)
            break
        if i+1 < len(arr) and (arr[i+1] == ')' or arr[i+1] == ']') and len(stack) != len(arr)-i:
            stay = stay*now[0]
        else:
            if len(stack) == 0:
                S = (S + stay)*now[0]
                res += S
                S = 0
                stay=1
            elif len(stack) != 0 and len(stack) == len(arr)-i-1: #현스택 == 남은길이
                stay = (S+stay)*now[0]
                S = 0
            else:
                S += stay*now[0]
                stay =1
else:
    print(res)

        
