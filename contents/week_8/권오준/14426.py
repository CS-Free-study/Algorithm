import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [input().rstrip() for _ in range(n)]
b = [input().rstrip() for _ in range(m)]
ans = 0

for i in b:
    for j in a:
        if i == j[ : len(i)]:
            ans += 1
            break

print(ans)