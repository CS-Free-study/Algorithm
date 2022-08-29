import sys
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    if i + s[i][0] > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], s[i][1] + dp[i + s[i][0]])

print(dp[0])