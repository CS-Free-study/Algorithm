# 백준 1541, 잃어버린 괄호, 실버2
import sys
input = sys.stdin.readline

command = list(input().rstrip().split('-'))
ans = 0

for i in command[0].split('+'):
    ans += int(i)

for i in command[1:]:
    for j in i.split('+'):
        ans -= int(j)

print(ans)