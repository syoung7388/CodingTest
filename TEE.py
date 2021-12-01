from collections import deque
Q = deque()
Q.append((1, 2, 3))
Q.append((2, 3, 4))
Q = sorted(Q)
print(Q.popleft())
