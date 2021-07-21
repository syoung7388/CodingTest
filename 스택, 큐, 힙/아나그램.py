
#아나그램


if __name__ == "__main__":
    w1= input()
    w2 = input()

    str1 = [0]*52
    str2 = [0]*52


    for x in w1:
        if x.isupper():
            str1[ord(x) - 65] += 1
        else:
            str1[ord(x) - 71] += 1

    for x in w2:
        if x.isupper():
            str2[ord(x) - 65] += 1
        else:
            str2[ord(x) - 71] += 1
    for i in range(52):
        if str1[i] != str2[i]:
            print("NO")
            break
    else:
        print("YES")

    
            


        
    
        
