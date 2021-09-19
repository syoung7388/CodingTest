word = []

while  True:
    w = input()

    if w == '-':
        break
    word.append(w)

while True:
    puz = [0]*26
    s = input()
    if s == '#':
        break

    
    for p in s:
        puz[ord(p)-65] += 1
    anw = [0]*26

    res = {}
    for i in s: # 선택단어
        res[i] = 0
        for w in word:
            if i not in w: continue
            ch = puz[:]
            for j in w:
                if ch[ord(j) -65] == 0:
                    break
                else:
                    ch[ord(j)-65] -= 1
            else:
                res[i] += 1
    res= sorted(res.items(), key = lambda x : (x[1],x[0]))
    Min = res[0][1]
    Max = res[-1][1]

    r1= ""
    r2 = ""



    for r in res:
        if r[1] == Min:
            r1 += r[0]
        if r[1] == Max:
            r2 += r[0]
    print(r1,Min, r2, Max)

    
            


    
