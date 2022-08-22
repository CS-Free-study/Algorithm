import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = []

for i in range(1, k + 1):
    a.append(int(str(n * i)[::-1]))

print(max(a))