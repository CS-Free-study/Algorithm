import sys
input = sys.stdin.readline

n, k = map(int, input().split())
c = list(range(1, n + 1))
ans = []
index = 0

for _ in range(n):
    index += k - 1

    if index >= len(c):
        index %= len(c)

    ans.append(c.pop(index))

print('<', ', '.join(map(str, ans)), '>', sep = '')