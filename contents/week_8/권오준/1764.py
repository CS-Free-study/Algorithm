import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = set()
b = set()
c = set()

for _ in range(n):
    a.add(input().rstrip())

for _ in range(m):
    b.add(input().rstrip())

c = a & b

print(len(c))
print('\n'.join(sorted(c)))