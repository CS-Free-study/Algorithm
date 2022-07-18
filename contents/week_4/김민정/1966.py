#1966 프린터 큐
#실버 3

import sys
from collections import deque
input = sys.stdin.readline
output = []

k = int(input()) #테스트 개수
for _ in range(k):
    n, m = map(int, input().split())
    printer = deque(map(int, input().split()))
    idx = deque(range(len(printer)))
    idx[m] = 'target'
    cnt = 0
    for _ in range(len(printer)):
        j = 1
        while j < len(printer):
            if printer[0] < printer[j]:
                printer.append(printer.popleft())
                idx.append(idx.popleft())
                j = 1
            else:
                j += 1

        if idx[0] == 'target':
            output.append(cnt+1)
            break
        else:
            printer.popleft()
            idx.popleft()
            cnt += 1
for i in range(len(output)):
    print(output[i])



