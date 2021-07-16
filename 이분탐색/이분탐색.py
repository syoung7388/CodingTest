
#N개 오름차순 정렬 -> M의 인덱스 ?


def chOrd(lt, rt):
    if lt < rt:
        s = (lt + rt) //2
        chOrd(lt,s)
        chOrd(s+1, rt)
        p1 = lt
        p2 = s+1
        res = list()
        while p1 <= s and p2 <= rt:
            if nums[p1] < nums[p2]:
                res.append(nums[p1])
                p1 += 1
            else:
                res.append(nums[p2])
                p2+= 1
        if p1 <= s: res += nums[p1:s+1]
        if p2 <= rt: res+= nums[p2:rt+1]
        for i in range(len(res)):
            nums[lt+i] = res[i]

                


if __name__ == "__main__":

    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    chOrd(0, N-1)

    l = 0
    r = N-1
    while True:
        mid = (l+r)//2
        if nums[mid] > M:
            r = mid-1
        elif nums[mid] < M:
            l = mid+1
        else:
            print(mid+1)
            break
        
