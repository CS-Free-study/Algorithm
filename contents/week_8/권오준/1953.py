import sys
input = sys.stdin.readline

n = int(input())
s = input().rstrip()
o = [int(input()) for _ in range(n)]
stk = []

for i in s:
    if 'A' <= i <= 'Z':
        stk.append(o[ord(i) - ord('A')])
    else:
        b = stk.pop()
        a = stk.pop()

        if i == '*':
            stk.append(a * b)
        elif i == '+':
            stk.append(a + b)
        elif i == '-':
            stk.append(a - b)
        elif i == '/':
            stk.append(a / b)

print("%.2f" % stk.pop())
