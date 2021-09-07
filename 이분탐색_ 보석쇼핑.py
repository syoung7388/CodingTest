
def solution(gems):
    cnt = len(set(gems))
    D = {gems[0]:1}
    N = len(gems)
    anw = [0, N-1]

    lt, rt = 0, 0
    while lt < N and rt < N:
        if len(D) == cnt:
            if rt-lt < anw[1]-anw[0]:
                anw = [lt, rt]
            if D[gems[lt]] == 1:
                del D[gems[lt]]
            else:
                D[gems[lt]] -= 1
            lt += 1
        else:
            rt += 1
            if rt == N:
                break
            if gems[rt] in D.keys():
                D[gems[rt]] += 1
            else:
                D[gems[rt]] = 1
    return [anw[0]+1, anw[1]+1]
                

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
