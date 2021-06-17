'''
체스판에서 이동
- L자로 이동
-밖에 못나감
- 수평 2칸 & 수직 한칸 || 수직 두칸 & 수평 한칸

나이트 위치가 주어졌을때 이동할 수 있는 경우의 수는 ?

'''

input_data = input("문자숫자형식:")
row = int(input_data[1]) #숫자
column = int(ord(input_data[0])) - int(ord('a')) +1


steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2,1),
         (1,2),(-1,2),(-2,1)]
result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >=1 and next_column <= 8:
        result += 1
print(result)