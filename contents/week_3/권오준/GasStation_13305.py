# 백준 13305, 주유소, 실버4
import sys
input = sys.stdin.readline

n = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))

min = costs[0]
result = 0

for i in range(n - 1):
    if min > costs[i]:
        min = costs[i]
    result += min * roads[i]

print(result)