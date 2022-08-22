# 백준 15486번 퇴사 2
# SILVER 1
# 알고리즘 분류 : 다이나믹 프로그래밍
# 뒤에서부터 탐색하는게 핵심 포인트
import sys
input = sys.stdin.readline
N = int(input())
li = [list(map(int,input().split())) for _ in range(N)]
dp = [0]*(N+1)
max_val = 0
for i in range(N-1,-1,-1) :
    if li[i][0] + i <= N :
        dp[i] = max(dp[i+li[i][0]]+li[i][1],max_val)
    else :
        dp[i] = max_val
    max_val = max(dp[i],max_val)
print(dp[0])