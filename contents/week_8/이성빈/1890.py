# 백준 1890번 점프
# SILVER 1
# 알고리즘 분류 : 다이나믹 프로그래밍
# 최단 거리로 가는 횟수를 구하는줄 알았는데, 도착지에 갈 수 있는 경로의 합을 구하는 문제.
import sys
input = sys.stdin.readline
N = int(input())
dp = [[0]*N for _ in range(N)]
li = [list(map(int,input().split())) for _ in range(N)]
dp[0][0] = 1
for i in range(N) :
    for j in range(N) :
        if li[i][j] == 0 :
            continue
        if i + li[i][j] < N :
            dp[i+li[i][j]][j] += dp[i][j]
        if j + li[i][j] < N :
            dp[i][j+li[i][j]] += dp[i][j]
print(dp[-1][-1])