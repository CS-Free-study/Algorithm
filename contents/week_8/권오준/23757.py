import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, m = map(int, input().split())
h = []

for i in list(map(int, input().split())):
    heappush(h, -i)

c = list(map(int, input().split()))

for i in c:
    p = -heappop(h)

    if p - i < 0:
        print(0)
        exit()
    else:
        heappush(h, -(p - i))

print(1)