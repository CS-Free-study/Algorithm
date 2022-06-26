# 백준 9012, 괄호, 실버4
import sys

n = int(sys.stdin.readline())

for i in range(n):
    command = sys.stdin.readline().strip()

    stack = []
    for bracket in command:
        if bracket == '(':
            stack.append(bracket)
        else:
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        print("NO" if stack else "YES")
