# 백준 9465, 스티커, 실버1
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    dp = [list(map(int, input().split())) for _ in range(2)]

    for j in range(1, n):
        if j == 1:
            dp[0][j] += dp[1][j - 1]
            dp[1][j] += dp[0][j - 1]
        else:
            dp[0][j] += max(dp[1][j - 1], dp[1][j - 2])
            dp[1][j] += max(dp[0][j - 1], dp[0][j - 2])
    
    print(max(dp[0][-1], dp[1][-1]))

