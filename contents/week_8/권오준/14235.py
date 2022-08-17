import sys
from heapq import heappush, heappop
input = sys.stdin.readline

h = []

for _ in range(int(input())):
    a = list(map(int, input().split()))

    if a[0] == 0:
        if h:
            print(-heappop(h))
        else:
            print(-1)
    else:
        for i in range(1, a[0] + 1):
            heappush(h, -a[i])