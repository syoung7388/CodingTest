




if __name__ == "__main__":
    gra = list(map(str, input()))
    stack = list()
    L=0
    S = 0
    while L < len(gra):
        if gra[L] == '(' and gra[L+1] == ')':
            for s in range(len(stack)):
                stack[s] += 1
            L += 2
        elif gra[L] == '(' and gra[L+1] == '(':
            stack.append(0)
            L += 1

        if gra[L] == ')':
            S += (stack.pop()+1)
            L+=1
    print(S)
            
            
