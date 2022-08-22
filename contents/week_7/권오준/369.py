import sys
input = sys.stdin.readline

n = int(input())
cnt = 0

for i in range(1, n + 1):
    for j in str(i):
        if j in '369':
            cnt += 1

print(cnt)