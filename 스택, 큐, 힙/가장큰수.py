



if __name__ == "__main__":
    nums, M = map(int, input().split())
    num = list(map(int, str(nums)))    
    stack = []
    for n in num:
        while stack and M > 0 and stack[-1] < n:
            stack.pop()
            M-=1
        stack.append(n)
    if M != 0:
        stack = stack[:-M]
    print(''.join(map(str, stack)))
            
            

    
    
