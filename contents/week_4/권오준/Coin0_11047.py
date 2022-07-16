# 백준 11047, 동전0, 실버4
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

ans = 0

for i in range(n - 1, -1, -1):
    if coins[i] > k:
        continue
    else:
        ans += k // coins[i]
        k = k % coins[i]

print(ans)