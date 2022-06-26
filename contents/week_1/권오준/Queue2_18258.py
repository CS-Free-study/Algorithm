# 백준 18258, 큐2, 실버4
import sys
from collections import deque

queue = deque()
n = int(sys.stdin.readline())

for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == "push":
        queue.append(command[1])
    elif command[0] == "pop":
        print(queue.popleft() if queue else -1)
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        print(0 if queue else 1)
    elif command[0] == "front":
        print(queue[0] if queue else -1)
    elif command[0] == "back":
        print(queue[-1] if queue else -1)
