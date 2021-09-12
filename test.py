import math
def solution(fees, records):
    
    In =[]
    Out = []
    for r in records:
        t, n, info = r.split()
        t1, t2 = map(int, t.split(':'))
        t = t1*60+t2
        if info == "IN":
            In.append((int(n), t))
        else:
            Out.append((int(n), t))

    In.sort(reverse = True)
    Out.sort(reverse = True)

    res = {}


    while In and Out:
        if In[-1][0] == Out[-1][0]:
            i = In.pop()
            o = Out.pop()
            time = o[1]-i[1]
        else:
            i = In.pop()
            time = 1439-i[1]

        if i[0] in res:
            res[i[0]] += time
        else:
            res[i[0]] = time

    if In:
        i = In.pop()
        time = 1439-i[1]
        if i[0] in res:
            res[i[0]] += time
        else:
            res[i[0]] = time


    r = []
    for idx, v in res.items():
        if v <= fees[0]:
            money = fees[1]
        else:
            money = fees[1]+math.ceil((v-fees[0])/fees[2])*fees[3]

        r.append(money)
    return r           


#print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]))
print(solution(	[1, 461, 1, 10], ["00:00 1234 IN"]))
