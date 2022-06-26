# 백준 1158, 요세푸스 문제, 실버4
import sys

n, k = map(int, sys.stdin.readline().split())

people = list(range(1,n + 1))
array = []
num = 0

for i in range(n):
    num += k - 1
    if num >= len(people):
        num = num % len(people)
    
    array.append(str(people.pop(num)))

print('<', ', '.join(array), '>', sep = '')