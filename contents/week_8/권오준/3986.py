import sys
input = sys.stdin.readline

ans = 0

for _ in range(int(input())):
    s = input().rstrip()
    stk = []

    for i in s:
        if stk and i == stk[-1]:
            stk.pop()
        else:
            stk.append(i)

    if not stk:
        ans += 1

print(ans)
    