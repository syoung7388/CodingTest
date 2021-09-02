
def changeS(time):
    h, m, s = time.split(':')
    return h*60*60 + m *60+ s

def Res(s):
    return '{:02d}:{:02d}:{:02d}'.format(s//3600, s%3600//60,s%3600%60 )

def solution(play_time, adv_time, logs):

    adv_time = changeS(adv_time)

    dp = [0]*360001

    for l in logs:
        st = changeS(l[0])
        ed = changeS(l[1])
        dp[st] += 1
        dp[ed] -= 1

    for j in range(1, 360001):
        dp[j] += dp[j-1]


    maxl, maxs = 0, dp[:adv_time]
    s = maxs

    for i in range(1, 360001):

        s = s-dp[i-1]+dp[i+adv_time]

        if s > maxs:
            maxl = i
            maxs = s
            
    return Res(maxl)


        

        
