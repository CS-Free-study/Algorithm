import sys
from heapq import heappush, heappop
input = sys.stdin.readline

h = []

for _ in range(int(input())):
    n = int(input())

    if n != 0:
        heappush(h, (abs(n), n))
    else:
        print(heappop(h)[1]) if h else print(0)