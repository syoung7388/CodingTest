


if __name__ == "__main__":

    N,M = map(int, input().split())
    N = list(map(int, str(N)))
    stack = []
    stack.append(N[0])

    
    for n in N:
        while stack and M > 0 and N[-1] < n:
            stack.pop()
            M-=1
        stack.append(n)

    if M != 0:
        stack = stack[:-M]
    for s in stack:
        print(s, end=" ")
        
        
        
