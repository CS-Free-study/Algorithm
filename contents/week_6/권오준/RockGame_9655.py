#백준 9655, 돌 게임, 실버5
import sys
input = sys.stdin.readline

n = int(input())

print('SK') if n % 2 == 1 else print('CY')