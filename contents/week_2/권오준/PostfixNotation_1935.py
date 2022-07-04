# 백준 1935, 후위 표식2, 실버3
''' 기존 방식
import sys

stack = []
cnt = 65
n = int(sys.stdin.readline())
p_n = list(sys.stdin.readline().rstrip())

for i in range(n):
    num = int(sys.stdin.readline())

    for j in range(i, len(p_n)):
        if not isinstance(p_n[j], int):
            if ord(p_n[j]) == cnt:
                p_n[j] = num
        
    cnt += 1

for i in range(len(p_n)):
    if isinstance(p_n[i], int):
        stack.append(p_n[i])
    elif p_n[i] == '+':
        stack.append(stack.pop() + stack.pop())
    elif p_n[i] == '-':
        second = stack.pop()
        first = stack.pop()
        stack.append(first - second)
    elif p_n[i] == '*':
        stack.append(stack.pop() * stack.pop())
    else:
        second = stack.pop()
        first = stack.pop()
        stack.append(first / second)

print("{:.2f}".format(stack.pop()))
'''

# 개선한 방식
import sys

n = int(sys.stdin.readline())
p_n = sys.stdin.readline().rstrip()

nums = [0] * n
stack = []

for i in range(n):
    nums[i] = int(sys.stdin.readline())

for i in p_n:
    if i >= 'A' and i <= 'Z':
        stack.append(nums[ord(i) - ord('A')])
    else:
        second = stack.pop()
        first = stack.pop()
        if i == '+':
            stack.append(first + second)
        elif i == '-':
            stack.append(first - second)
        elif i == '*':
            stack.append(first * second)
        elif i == '/':
            stack.append(first / second)

print("%.2f" % stack.pop())