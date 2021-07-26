cards = list(range(21)) #0~20
for i in range(10):
    ra,rb = map(int, input().split())
    size = rb - ra +1
    for j in range(size//2):
        cards[ra + j], cards[rb-j] = cards[rb-j], cards[ra + j]

cards.pop(0)
for c in cards:
    print(c, end=" ")








