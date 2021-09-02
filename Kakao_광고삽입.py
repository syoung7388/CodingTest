
def changeS(s):
    h, m, s = map(int, s.split(':'))
    return h*60*60+m*60+s
def Res(s):

    h, m, s = s//(60*60), (s%(60*60))//60, (s%(60*60))%60
    return '{:02d}:{:02d}:{:02d}'.format(h, m, s)    
def solution(play_time, adv_time, logs):
    if play_time <= adv_time:
        return "00:00:00"
    
    play_time = changeS(play_time)
    adv_time = changeS(adv_time)
    ch = [0]*(360001)
    temp= []
    for l in logs:
        time = l.split('-')
        t1 = changeS(time[0])
        t2 = changeS(time[1])
        ch[t1] += 1
        ch[t2] -= 1
    for l in range(1, 360001):
        ch[l] += ch[l-1]

    maxid = 0
    maxad = sum(ch[:adv_time])
    s = maxad
    for i in range(1, 360001-adv_time):
        s = s-ch[i-1]+ch[i+adv_time-1]
        if s > maxad:
            maxad = s
            maxid = i
    return Res(maxid)
    
#print(solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))           
print(solution("99:59:59","25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))       
        
        
