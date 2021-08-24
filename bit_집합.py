
bit= 0

for _ in range(int(input())):
    order = list(map(str, input().split()))
    
    if order[0] == "all":
        bit = (1<<20) -1
    elif order[0] == "empty":
        bit = 0
    else:
        n = int(order[1])-1
        if order[0] == "add":
            bit |= (1<<n)
        elif order[0] == "remove":
            bit &= ~(1<<n)
        elif order[0] == "check":
            if bit & (1<<n) == 0:
                print(0)
            else:
                print(1)
        elif order[0] == "toggle":
            bit = bit ^(1<<n)
