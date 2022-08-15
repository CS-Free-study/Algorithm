import sys
input = sys.stdin.readline

n = int(input())

if n % 10 != 0:
    print(-1)
else:
    a = n // 300
    b = n % 300 // 60
    c = n % 300 % 60 // 10
    print(a, b, c)