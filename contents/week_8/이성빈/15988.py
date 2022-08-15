# 백준 15988번 1,2,3 더하기 3
# SILVER 2
# 알고리즘 분류 : 다이나믹 프로그래밍
# 다 구한뒤 테스트 케이스에서 원하는 값을 출력
import sys
input = sys.stdin.readline
T = int(input())
dp = [1,2,4] + [0]*999999
for i in range(3,1000001) :
    dp[i] = (dp[i-3] + dp[i-2] + dp[i-1])%1000000009

for _ in range(T) :
    n = int(input())
    print(dp[n-1])