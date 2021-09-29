


def GDB(a, b):
    print(a, b)
    if a%b == 0:
        print(b)
        return b
    return GDB(b, a%b)


N, M = map(int, input().split())
print(M- GDB(N, M))
