import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().rstrip()
    stack = []

    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        print('NO' if stack else 'YES')