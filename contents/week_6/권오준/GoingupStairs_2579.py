# 백준 2579, 계단 오르기, 실버3
import sys
input = sys.stdin.readline

n = int(input())
score = [int(input()) for _ in range(n)]
dp = [0] * n

if n == 0:
    print(0)
elif n == 1:
    print(score[0])
elif n == 2:
    print(score[0] + score[1])
else:
    dp[0] = score[0]
    dp[1] = score[0] + score[1]
    dp[2] = max(score[0] + score[2], score[1] + score[2])

    for i in range(3, n):
        dp[i] = max(dp[i - 3] + score[i - 1] + score[i], dp[i - 2] + score[i])

    print(dp[-1])