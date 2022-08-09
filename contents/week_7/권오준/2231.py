import sys
input = sys.stdin.readline

n = int(input())
ans = 0

for i in range(1, n + 1):
    m = list(map(int, str(i)))
    ans = i + sum(m)

    if ans == n:
        print(i)
        break

    if i == n:
        print(0)
