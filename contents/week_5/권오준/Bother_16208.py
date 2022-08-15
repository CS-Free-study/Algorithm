# 백준 16208, 귀찮음, 실버5
import sys
input = sys.stdin.readline

n = int(input())
rods = list(map(int, input().split()))

rods.sort()
total = sum(rods)
ans = 0

for i in rods:
    total -= i
    ans += i * total

print(ans)