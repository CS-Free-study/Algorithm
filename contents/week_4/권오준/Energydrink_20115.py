# 백준 20115, 에너지 드링크, 실버3
import sys
input = sys.stdin.readline

n = int(input())
drinks = list(map(int, input().split()))

drinks.sort()
ans = drinks[-1]

for i in range(n - 1):
    ans += drinks[i] / 2

print(ans)