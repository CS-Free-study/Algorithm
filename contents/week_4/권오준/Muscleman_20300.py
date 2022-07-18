# 백준 20300, 서강근육맨, 실버3
import sys
input = sys.stdin.readline

n = int(input())
muscles = list(map(int, input().split()))

muscles.sort()
ans = []

if len(muscles) % 2 == 1:
    ans.append(muscles[-1])
    muscles.pop()
else:
    ans.append(0)

for i in range(len(muscles) // 2):
    ans.append(muscles[i] + muscles[-(i + 1)])

print(max(ans))