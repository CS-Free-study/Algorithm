import sys
input = sys.stdin.readline

d = {}

for _ in range(int(input())):
    a, b = map(str, input().rstrip().split())

    if b == 'enter':
        d[a] = True
    else:
        del d[a]

for i in sorted(d, reverse = True):
    print(i)
        