# 백준 10799, 쇠막대기, 실버 3
import sys

command = list(sys.stdin.readline().rstrip())

stack = []
rod = 0

for i in range(len(command)):
    if command[i] == '(':
        stack.append('(')
    else:
        stack.pop()
        if command[i - 1] == '(':
            rod += len(stack)
        else:
            rod += 1

print(rod)