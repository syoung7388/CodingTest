def DFS(id, n, G, ch, s):
    global answer
    if ch.count(1) > answer:
        return
    if id == len(G):
        arr = [0]*n
        tmp = 0
        for j in range(len(G)):
            if ch[j] == 1:
                for g in range(G[j][0]-1, G[j][1]):
                    arr[g] = 1
                tmp += 1
        cnt = tmp + arr.count(0)
        if cnt < answer:
            answer = cnt
        return
    else:
        for i in range(s,len(G)):
            ch[i] = 1
            DFS(id+1, n, G, ch, i+1)
            ch[i] = 0
            DFS(id+1, n, G, ch, i+1)
def solution(n, groups):
    ch = [0]*(len(groups))
    DFS(0, n, groups, ch, 0)
    print(answer)
    return answer
if __name__ == "__main__":
    answer = 2147000000
    solution(5, [[1,2],[2,3],[1,3]])

