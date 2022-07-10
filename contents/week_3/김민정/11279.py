#11279 최대 힙
#실버2
import heapq
import sys

n = int(sys.stdin.readline())
max_heap = [] #최대 힙


for _ in range(n):
    x = int(sys.stdin.readline())
    if x > 0 :
        heapq.heappush(max_heap,(-x,x))
    else:
        if len(max_heap) == 0:
            print(0)
        else:
            max_num = heapq.heappop(max_heap)[1]
            print(max_num)



