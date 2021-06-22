msg = "IT is True"

print(msg.upper())
print(msg.lower())
print(msg.find("T"))
print(msg.count("T"))
print(msg[:2])
print(msg[3:7])

for m in range(len(msg)):
    print(msg[m], end=" ")
print()
for m in msg:
    if m.islower():
        print(m, end=" ")
print()

#아스키코드 A(65)~Z(90)
for m in msg:
    if m.isalpha():
        print(m , end=" ")
print()
for m in msg:
    print(ord(m), end=" ")
print()
print(chr(68))





