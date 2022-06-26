# 백준 1874, 스택 수열, 실버2
import sys

n = int(sys.stdin.readline())
stack = []
operations = []
cnt = 1
possible = True

for _ in range(n):
    num = int(sys.stdin.readline())
    
    while cnt <= num:
        stack.append(cnt)
        operations.append('+')
        cnt += 1
    
    if num == stack[-1]:
        stack.pop()
        operations.append('-')
    else:
        possible = False

print('\n'.join(operations) if possible else 'NO')