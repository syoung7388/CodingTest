
def isP(x):
    for i in range(2, x):
        if x%i== 0:
            return False
    return True

a = [12, 13, 17, 18, 19, 29]

for x in a:
    if isP(x):
        print(x, end=" ")