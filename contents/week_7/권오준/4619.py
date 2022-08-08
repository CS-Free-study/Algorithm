import sys
input = sys.stdin.readline

while True:
    b, n = map(int, input().split())

    if b == n == 0:
        break
    
    i = 0
    while i ** n < b:
        i += 1

    if abs(b - i ** n) > abs(b - (i - 1) ** n):
        print(i - 1)
    else:
        print(i)