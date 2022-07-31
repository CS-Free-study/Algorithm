# 백준 2407, 조합, 실버4
import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())

print(math.factorial(n) // (math.factorial(n - m) * math.factorial(m)))