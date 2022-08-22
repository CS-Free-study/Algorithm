import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    a = set(int(input()) for _ in range(n))
    b = set(int(input()) for _ in range(m))

    print(len(a & b))