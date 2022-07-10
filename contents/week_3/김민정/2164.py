#2164 카드 2
#큐 구현

import sys
from collections import deque

n = int(sys.stdin.readline())

card = deque([i for i in range(1, n+1)])

while len(card) > 1:
    card.popleft()
    card.append(card[0])
    card.popleft()
print(card.pop())