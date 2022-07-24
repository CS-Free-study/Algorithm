# 백준 16435, 스네이크버드, 실버5
import sys
input = sys.stdin.readline

n, snake = map(int, input().split())
fruits = list(map(int, input().split()))

fruits.sort()

for i in fruits:
    if i <= snake:
        snake += 1

print(snake)