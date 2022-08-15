# 백준 1010, 다리 놓기, 실버5
import sys
import math
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    print(math.factorial(m) // (math.factorial(n) * math.factorial(m - n)))