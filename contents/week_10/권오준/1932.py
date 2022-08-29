import sys
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (i + 2) for i in range(n + 1)]
dp[0][0] = s[0][0]

for i in range(1, n):
    for j in range(i + 1):
        dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + s[i][j]

print(max(dp[n - 1]))