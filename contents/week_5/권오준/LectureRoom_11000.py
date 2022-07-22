# 백준 11000, 강의실 배정, 골드5
import sys
import heapq
input = sys.stdin.readline

n = int(input())
lectures = [list(map(int, input().split())) for _ in range(n)]

lectures.sort()
rooms = []
heapq.heappush(rooms, lectures[0][1])

for i in range(1, n):
    if lectures[i][0] >= rooms[0]:
        heapq.heappop(rooms)
        heapq.heappush(rooms, lectures[i][1])
    else:
        heapq.heappush(rooms, lectures[i][1])

print(len(rooms))