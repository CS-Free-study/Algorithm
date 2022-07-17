# 백준 1758, 알바생 강호, 실버4
import sys
input = sys.stdin.readline

n = int(input())
tips = list(int(input()) for _ in range(n))

tips.sort(reverse = True)

for i in range(n):
    tips[i] = tips[i] - i
    if tips[i] < 0:
        tips[i] = 0

print(sum(tips))