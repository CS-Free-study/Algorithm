import sys
input = sys.stdin.readline

a = [int(input()) for _ in range(10)]
total = 0

for i in a:
    total += i
    if total >= 100:
        if total - 100 > 100 - (total - i):
            total -= i
        break

print(total)