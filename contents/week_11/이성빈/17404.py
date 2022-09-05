# 백준 17404번 RGB거리 2
# GOLD 4
# 알고리즘 분류 : 다이나믹 프로그래밍
# RGB거리 에서 1번쨰와 N번째 색깔이 달라지는 조건이 추가된 문제
import sys
INF = sys.maxsize
input = sys.stdin.readline
N = int(input())
li = [list(map(int,input().split())) for _ in range(N)]
dp = [[0]*3 for _ in range(N)]
ans = INF
for k in range(3) :
    dp[0][k] = li[0][k]
    dp[0][k-1] = INF
    dp[0][k-2] = INF
    for i in range(1,N) :
        for j in range(3) :
            dp[i][j] = li[i][j] + min(dp[i-1][j-1],dp[i-1][j-2])
    ans = min(ans,dp[-1][k-1],dp[-1][k-2])
print(ans)