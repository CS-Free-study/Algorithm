# 백준 21313, 문어, 브론즈2
import sys
input = sys.stdin.readline

n = int(input())
ans = []

for i in range(n):
    ans.append(i % 2 + 1)

if n % 2 == 1:
    ans[-1] = 3

for i in ans:
    print(i, end = ' ')