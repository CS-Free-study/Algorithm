# 백준 1966, 프린터 큐, 실버3
import sys
from collections import deque

testCase = int(sys.stdin.readline())

for _ in range(testCase):
    n, m = map(int, sys.stdin.readline().split())
    printer = deque(map(int, sys.stdin.readline().split()))
    check = deque(0 for _ in range(n))
    check[m] = 1
    cnt = 0

    while True:
        if printer[0] == max(printer):
            cnt += 1

            if check[0] == 1:
                print(cnt)
                break
            else:
                printer.popleft()
                check.popleft()

        else:
            printer.append(printer.popleft())
            check.append(check.popleft())