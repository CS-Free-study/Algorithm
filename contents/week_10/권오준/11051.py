import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [[1] * i for i in range(1, n + 2)]

for i in range(2, n + 1):
    for j in range(1, i):
        dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % 10007

print(dp[n][k])