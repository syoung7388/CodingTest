
import sys
Ipv6 = input()



Ipv6 = Ipv6.split(':')

center = []

print(Ipv6)
if Ipv6[-1] == '':
    Ipv6.pop()
if Ipv6[0] == '':
    Ipv6.pop(0)



for i in range(len(Ipv6)):

    L = len(Ipv6[i])
    if Ipv6[i] == '':
        center.append(i)
    elif L < 4:
        ns ='0'*(4-L)+Ipv6[i]
        Ipv6[i] = ns

    
if center:
    Ipv6[center[0]] = '0000'
    if len(center) == 2:
        Ipv6[center[1]] = '0000'

        
    cha = 8-(len(Ipv6))
    for _ in range(cha):
        Ipv6.insert(center[0], '0000')

print(':'.join(Ipv6)) 
