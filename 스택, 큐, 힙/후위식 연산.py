if __name__ == "__main__":
    sik = input()
    stack = list()
    for x in sik:
        if x.isdigit():
            stack.append(x)
        else:
            b = int(stack.pop())
            a = int(stack.pop())
            if x == '+':
                stack.append(a+b)
            if x == '-':
                stack.append(a-b)
            if x == '*':
                stack.append(a*b)
            if x == '/':
                stack.append(a/b)

    print(stack[0])
        
