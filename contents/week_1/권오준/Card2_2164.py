# 백준 2164, 카드2, 실버4
import sys
from collections import deque

n = int(sys.stdin.readline())
cards = deque(range(1, n + 1))

for _ in range(n - 1):
    cards.popleft()
    cards.append(cards.popleft())

print(cards.pop())