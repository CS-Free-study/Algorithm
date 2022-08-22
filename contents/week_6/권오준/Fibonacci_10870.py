# 백준 10870, 피보나치 수5, 브론즈5
import sys
input = sys.stdin.readline

n = int(input())
num = [0, 1]

for i in range(2, n + 1):
    num.append(num[i - 2] + num[i - 1])

print(0) if n == 0 else print(num[-1])

# 함수 사용
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)

print(fibo(n))