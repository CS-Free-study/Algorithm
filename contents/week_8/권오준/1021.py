import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
q = deque(range(1, n + 1))
cnt = 0

for i in nums:
    while True:
        if i == q[0]:
            q.popleft()
            break

        if q.index(i) < len(q) / 2:
            q.append(q.popleft())
        else:
            q.appendleft(q.pop())
        cnt += 1

print(cnt)