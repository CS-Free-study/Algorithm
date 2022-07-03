# 백준 1021, 회전하는 큐, 실버4
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

num = list(map(int, sys.stdin.readline().split()))

queue = deque(range(1, n + 1))
cnt = 0

for i in num:
    while True:
        if i == queue[0]:
            queue.popleft()
            break
        else:
            if queue.index(i) < len(queue) / 2:
                queue.append(queue.popleft())
            else:
                queue.appendleft(queue.pop())
            cnt += 1

print(cnt)
