import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0] * 3 for _ in range(m)] for _ in range(n)]
ans = 1e9

for i in range(m):
    for j in range(3):
        dp[0][i][j] = s[0][i]

for i in range(1, n):
    for j in range(m):
        if j == 0:
            dp[i][j][1] = dp[i - 1][j + 1][0] + s[i][j]
            dp[i][j][2] = min(dp[i - 1][j][1], dp[i - 1][j + 1][0]) + s[i][j]
        elif j == m - 1:
            dp[i][j][0] = min(dp[i - 1][j][1], dp[i - 1][j - 1][2]) + s[i][j]
            dp[i][j][1] = dp[i - 1][j - 1][2] + s[i][j]
        else:
            dp[i][j][0] = min(dp[i - 1][j][1], dp[i - 1][j - 1][2]) + s[i][j]
            dp[i][j][1] = min(dp[i - 1][j + 1][0], dp[i - 1][j - 1][2]) + s[i][j]
            dp[i][j][2] = min(dp[i - 1][j + 1][0], dp[i - 1][j][1]) + s[i][j]

for i in range(m):
    for j in range(3):
        if dp[n - 1][i][j] != 0:
            ans = min(ans, dp[n - 1][i][j])

print(ans)