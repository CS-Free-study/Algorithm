# 1927 최소힙
import sys
import heapq
from sys import stdin
from collections import deque

arr = []
heapq.heapify(arr)


n = int(sys.stdin.readline())
for _ in range(n):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(arr, x)
    else:
        if len(arr) == 0:
            print(0)
        else:
            result = heapq.heappop(arr)
            print(result)
