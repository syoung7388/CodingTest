


def solution(N, number):
    dp = [[]]

    for i in range(1, 9):
        temp = []
        for j in range(1, i):
            for k in dp[j]:
                for l in dp[i-j]:
                    print(k, l)
                    temp.append(k+l)
                    if k-l>= 0:
                        temp.append(k-l)
                    temp.append(k*l)
                    if l != 0 and k != 0:
                        temp.append(k//l)
        temp.append(int(str(N)*i))

        if number in temp:
            return i
        dp.append(list(set(temp)))
        print(dp)
    return -1


print(solution(5, 12))
