def solution(N, number):
    dy = [set() for _ in range(10)]
    for l in range(1, 10):
        dy[l].add(int(str(N)*l))
    for i in range(1, 10):
        for j in range(1, i//2+1):
            for n1 in dy[j]:
                for n2 in dy[i-j]:
                    dy[i].add(n1+n2)
                    dy[i].add(n1-n2)
                    dy[i].add(n2-n1)
                    dy[i].add(n2*n1)
                    if n1 > 0:
                        dy[i].add(n2//n1)
                    if n2 > 0:
                        dy[i].add(n1//n2)
            if number in dy[i]:
                return i
    return -1

print(solution(5, 12))
