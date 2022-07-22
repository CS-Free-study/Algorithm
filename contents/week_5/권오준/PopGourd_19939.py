# 백준 19939, 박 터뜨리기, 실버5
import sys
input = sys.stdin.readline

n, p = map(int, input().split())

min = p * (p + 1) // 2
if n < min:
    print(-1)
elif (n - min) % p == 0:
    print(p - 1)
else:
    print(p)