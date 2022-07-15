# 백준 1931, 회의실 배정, 실버1
import sys
input = sys.stdin.readline

n = int(input())
meetings = [list(map(int, input().split())) for _ in range(n)]

meetings.sort()
meetings.sort(key = lambda x:x[1])

end = 0
ans = 0

for i in range(n):
    if meetings[i][0] >= end:
        end = meetings[i][1]
        ans += 1

print(ans)