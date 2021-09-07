import heapq
def solution(n, k, cmd):

    left, right, delete = [], [], []

    #오른쪽은 최솟값이 맨앞에 위치
    for i in range(n):
        heapq.heappush(right, i)

    #왼쪽은 최댓값이 맨앞 위치
    for i in range(k):
        heapq.heappush(left, -heapq.heappop(right))


    for c in  cmd:
        if len(c) > 1:
            move = int(c.split()[-1])
            if c.startswith("D"):
                for _ in range(move):
                    #오른쪽 heap 에서 왼쪽 heap으로 값을 이동
                    if right:
                        heapq.heappush(left, -heapq.heappop(right))
            elif c.startswith("U"):
                for _ in range(move):
                    if left:
                        heapq.heappush(right, -heapq.heappop(left))
        elif c == "C":
            delete.append(heapq.heappop(right))
            if not right:
                heapq.heappush(right, -heapq.heappop(left))
        elif c == "Z":
            repair = delete.pop()

            if repair < right[0]:
                heapq.heappush(left, -repair)
            else:
                heapq.heappush(right, repair)

    result = ["O"]*n

    for d in delete:
        result[d] = "X"
    return "".join(result)
print(solution(8, 2 ,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
