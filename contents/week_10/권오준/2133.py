import sys
input = sys.stdin.readline

dp = [0] * 31
dp[2] = 3

for i in range(4, 31, 2):
    dp[i] = dp[i - 2] * 3 + sum(dp[:i - 3]) * 2 + 2

print(dp[int(input())])