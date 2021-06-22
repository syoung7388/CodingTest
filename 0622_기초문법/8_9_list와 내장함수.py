import random

a = []
a= list(range(1, 10))
a.append(11)
a.insert(3, 10)
a.insert(8, [9,4,3])
#print(a.pop(8))
#print(a.pop(2))
a.pop(8)
a.remove(10)
print(a.index(11))
print(sum(a))
print(max(a))
print(min(a))
random.shuffle(a)
a.sort()
a.sort(reverse=True)
#a.clear()
print("9 ====================")
a.sort()
a[0:7]
len(a)
for i in a:
    print(i, end=" ")
print()
for i in range(0,len(a)):
    print(a[i], end=" ")
print()
for i in enumerate(a):
    print(i, end=" ")
print()
for key, value in enumerate(a):
    print(key, value, end="/")
print()
a[3] = 10

if all(x> 8 for x in a):
    print("True")
else:
    print("False")
if any(x> 8 for x in a):
    print("True")
else:
    print("False")
