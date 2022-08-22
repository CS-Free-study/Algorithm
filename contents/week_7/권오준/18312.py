import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ans = 0

def convert(n):
    return '0' + str(n) if n < 10 else str(n)

for hour in range(n + 1):
    hour = convert(hour)
    for min in range(60):
        min = convert(min)
        for sec in range(60):
            sec = convert(sec)
            if str(k) in hour + min + sec:
                ans += 1

print(ans)