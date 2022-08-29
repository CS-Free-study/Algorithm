import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]

for i in range(m):
    dp[-1][i] = s[-1][i]

for i in range(n - 2, -1, -1):
    for j in range(m):
        if s[i][j] == 1:
            if j == 0:
                dp[i][j] = dp[i + 1][j] + dp[i + 1][j + 1]
            elif j == m - 1:
                dp[i][j] = dp[i + 1][j] + dp[i + 1][j - 1]
            else:
                dp[i][j] = dp[i + 1][j] + dp[i + 1][j - 1] + dp[i + 1][j + 1]

print(sum(dp[0]) % 1000000007)