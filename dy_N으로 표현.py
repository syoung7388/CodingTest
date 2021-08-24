def solution(N, number):
    dy = [set() for _ in range(9)] #최솟값이 8보다 크면 -1 return
    if N == number:
        return 1
    for l in range(1, 9):
        dy[l].add(int(str(N)*(l)))   
    for i in range(2, 9):
        for j in range(1, i//2+1):
            for x in dy[j]:
                for y in dy[i-j]:
                    dy[i].add(x+y)
                    dy[i].add(x-y)
                    dy[i].add(y-x)
                    dy[i].add(x*y)
                    if y != 0:
                        dy[i].add(x/y)
                    if x != 0:
                        dy[i].add(y/x)
            if number in dy[i]:
                return i
    return -1

