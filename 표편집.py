from bisect import bisect_left
def solution(N, K, cmd):
    arr = [x for x in range(N)]
    cur = K
    delete = []
    for c in cmd:
        if c == "C":
            delete.append(arr.pop(cur))
            if cur == len(arr):
                cur -= 1
        elif c == "Z":
            d = delete.pop()
            idx = bisect_left(arr, d)
            if d < arr[cur]:
                cur += 1
            arr.insert(idx, d)
        else:
            order, n = c.split(" ")
            n = int(n)
            if order == "D":
                cur = cur+n
            elif order == "U":
                cur = cur-n

        
    res = ["X"]*N
    for i in range(len(arr)):
        res[arr[i]] = "O"
    return "".join(res)
print(solution(8, 2 ,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
