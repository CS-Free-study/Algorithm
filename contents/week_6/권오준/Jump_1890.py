# 백준 1890, 점프, 실버 1
import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:
            print(dp[-1][-1])
            break
        if dp[i][j] > 0:
            num = board[i][j]

            if i + num < n:
                dp[i + num][j] += dp[i][j]
            if j + num < n:
                dp[i][j + num] += dp[i][j]