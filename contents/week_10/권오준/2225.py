import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [[1] * (n + 1) for _ in range(k + 1)]

for i in range(1, k + 1):
    dp[i][1] = i

for i in range(2, k + 1):
    for j in range(2, n + 1):
        dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000000

print(dp[-1][-1])