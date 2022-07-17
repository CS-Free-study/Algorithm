# 백준 11399, ATM, 실버4
# import sys
# input = sys.stdin.readline

# n = int(input())
# times = list(map(int, input().split()))

# wait = 0
# total = 0

# times.sort()

# for i in times:
#     wait += i
#     total += wait

# print(total)

# 다른 풀이
import sys
input = sys.stdin.readline

n = int(input())
times = list(map(int, input().split()))

total = 0

times.sort()

for i in range(1, n + 1):
    total += sum(times[0: i])

print(total)