def solution(money):
    dy1 = [0]*len(money)
    dy1[0] = money[0]
    dy1[1] = max(money[0], money[1])


    for i in range(2, len(money)-1):
        dy1[i] = max(dy1[i-1], money[i]+dy1[i-2])

        print(dy1)

    dy2 = [0]*len(money)
    dy2[0] = 0
    dy2[1] = money[1]



    for i in range(2, len(money)):
        dy2[i] = max(dy2[i-1], money[i]+dy2[i-2])
        print(dy2)
    return max(max(dy1), max(dy2))

print(solution([1, 2, 3, 1]))
    
