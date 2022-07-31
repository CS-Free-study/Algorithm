# 백준 17626, Four Squares, 실버3
import math
import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 50001

dp[0] = 0
dp[1] = 1

for i in range(2, n+1):
    min_value = 1e9

    for k in range(1, math.floor(math.sqrt(i)) + 1):
        min_value = min(min_value, dp[i - k * k])

    dp[i] = min_value + 1

print(dp[n])