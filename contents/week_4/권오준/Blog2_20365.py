# 백준 20365, 블로그2, 실버2
import sys
input = sys.stdin.readline

n = int(input())
command = input().rstrip()

colors = { 'B': 0, 'R': 0 }
colors[command[0]] += 1

for i in range(1, n):
    if command[i] != command[i - 1]:
        colors[command[i]] += 1

print(min(colors['B'], colors['R']) + 1)