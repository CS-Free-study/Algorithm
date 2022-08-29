import sys
input = sys.stdin.readline

dp = [[0] * 2 for _ in range(46)]
dp[0][0] = 1
dp[1][1] = 1

for i in range(2, 46):
    dp[i][0] = dp[i - 1][1]
    dp[i][1] = dp[i - 1][0] + dp[i - 1][1]

print(*dp[int(input())])