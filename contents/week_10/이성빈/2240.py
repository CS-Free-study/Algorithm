# 백준 2240번 자두나무
# GOLD 5
# 알고리즘 분류 : 다이나믹 프로그래밍
import sys
input = sys.stdin.readline
T,W = map(int,input().split())
dp = [[0]*(W+1) for _ in range(T+1)]
li = [0] + [int(input()) for _ in range(T)]
for i in range(1,T+1) :
    for j in range(W+1) :
        if (j+li[i])%2 == 1 :
            if j == 0 :
                dp[i][j] = dp[i-1][j] + 1
            else :
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]) + 1
        else :
            if j == 0 :
                dp[i][j] = dp[i-1][j]
            else :
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-1])
print(max(dp[-1]))