# 백준 2346, 풍선 터뜨리기, 실버3
import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque(enumerate(map(int, sys.stdin.readline().split())))
ans = []

while q:
    index, paper = q.popleft()
    ans.append(index + 1)

    if paper > 0:
        q.rotate(-(paper - 1))
    elif paper < 0:
        q.rotate(-paper)

print(' '.join(map(str, ans)))