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

    ch = puz[:]
    anw = [0]*26

    for ws in word:
        puz = ch[:]
        for w in ws:
            if puz[ord(w)-65] == 0:
                break
            else:
                puz[ord(w)-65] -=1
        else:
            for w in set(ws):
                anw[ord(w)-65] += 1
                


    Min = 2147000000
    Max = 0
    for i in range(26):
        if anw[i] == 0: continue
        if anw[i] < Min:
            Min = anw[i]
        if anw[i] > Max:
            Max = anw[i]

    res1 = ""
    res2 = ""
    for i in range(26):
        if anw[i] == Min:
            res1+=chr(i+65)
        if anw[i] ==Max:
            res2 += chr(i+65)
    print(res1, Min, res2, Max)
            
    
            
            


    
