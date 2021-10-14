#무거운 박스를 힘쎈애가 든다 !

C = int(input())
crains = list(map(int, input().split()))
B = int(input())
boxs = list(map(int, input().split()))
crains.sort(reverse = True)
boxs.sort(reverse = True)
if crains[0] < boxs[0]:
    print(-1)
    sys.exit(0)
cnt = 0
while boxs:
    cnt += 1
    for c in crains:
        for b in boxs:
            if b <= c:
                boxs.remove(b)
                break
print(cnt)
