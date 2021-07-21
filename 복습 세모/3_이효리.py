

if __name__ == "__main__":
    N = int(input())

    for n in range(N):
        w = input()

        for i in range(len(w)//2):
            if w[i].upper() != w[-1-i].upper():
                print("#%d NO" %(n+1))
                break
        else:
            print("#%d YES" %(n+1))
                
            
        
        
                
            
            
            
