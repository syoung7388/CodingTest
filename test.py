def seconds(s):
    h, m, s = map(int, s.split(":"))
    return h*3600+m*60+s
def hms(s):
    h, m, s = s//3600 , (s%3600)//60, (s%3600)%60
    return '{:02d}:{:02d}:{:02d}'.format(h, m, s)

def solution(play, adv, logs):
    play = seconds(play)
    adv = seconds(adv)
    if play <= adv:
        return "00:00:00"
    
    dp = [0]*(360001)
    
    for l in logs:
        st, ed= l.split("-")
        st = seconds(st)
        ed = seconds(ed)
        dp[st] += 1
        dp[ed] -= -1
    
    for i in range(1, 360001):
        dp[i] += dp[i-1]

    res= 0
    S = sum(dp[:adv]) #이전 합계
    maxad = S
    
    for j in range(1, 360001-adv):
        S = S - dp[j-1] + dp[j+adv-1]
        if S > maxad:
            res = j
            maxad = S
    print(j)
    return hms(res)
        
