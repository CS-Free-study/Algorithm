# 백준 2217, 로프, 실버4
import sys
input = sys.stdin.readline

n = int(input())
weights = []

for _ in range(n):
    weights.append(int(input()))

weights.sort(reverse = True)

for i in range(n):
    weights[i] = weights[i] * (i + 1)

print(max(weights))