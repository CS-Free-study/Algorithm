# 백준 2847, 게임을 만든 동준이, 실버4
import sys
input = sys.stdin.readline

n = int(input())
score = [int(input()) for _ in range(n)]

ans = 0

for i in range(n - 2, -1, -1):
    while score[i] >= score[i + 1]:
        score[i] -= 1
        ans += 1

print(ans)