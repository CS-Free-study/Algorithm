# 1026 보물
# 실버 4

from sys import stdin

read = stdin.readline

N = int(read())
sum = 0
A = list(map(int, read().split()))
B = list(map(int, read().split()))

A.sort(reverse=False)
B.sort(reverse=True)


for i in range(N):
    sum += A[i] * B[i]
print(sum)
