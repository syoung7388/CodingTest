a= [[0]*3 for _ in range(3)]
a[0][1] = 2
a[0][0] = 3
a[1][2] = 4

for x in a:
    for y in x:
        print(y, end=" ")
    print()
print(a)