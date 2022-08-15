# 백준 11055, 가장 큰 증가 부분 수열, 실버 2
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [0] * n

dp[0] = nums[0]

for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[j] + nums[i], dp[i])
        else:
            dp[i] = max(dp[i], nums[i])

print(max(dp))