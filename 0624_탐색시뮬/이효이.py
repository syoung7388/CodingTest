#앞으로 해도 이효리, 뒤로 해도 이효리
#쌤꺼 추천 직접 하라함
N = int(input())
for n in range(N):
    w = input()
    w.upper()
    size = len(w)
    for i in range(size//2):
        if w[i] != w[-1-i]:
            print("#%d NO" %(n+1))
            break
    else:
        print("#%d YES" %(n+1))
print()



"""
def Check_w (word):
    a = word.lower()
    b = word[::-1].lower()
    if a==b:
        return True
    else:
        return False
for n in range(N):
    word = input()
    if Check_w(word) == True:
        print("#%d %s"%(n+1,"YES"))
    else:
        print("#%d %s"%(n+1,"NO"))
"""
